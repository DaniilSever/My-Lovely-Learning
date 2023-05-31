import React, { useState, useRef } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Animated} from "react-native";
import Ionicons from 'react-native-vector-icons/Ionicons';
import { Settings } from '../../styles/style';

// content
import { change_profile, change_email, change_password } from './ScreenSettings';


export function SettingsScreen({navigation}) {
    const [currentTab, setCurrentTab] = useState("Редактировать профиль");
    // To get the curretn Status of menu ...
    const [showMenu, setShowMenu] = useState(false);
    const [content, setContent] = useState(change_profile)

    const offsetValue = useRef(new Animated.Value(0)).current;

    return (
        <View style={Settings.container}>
            <View style={Settings.menuContainer}>

                <Text style={Settings.menuTitle}>
                    Меню
                </Text>

                <View style={{ paddingLeft: 15, marginTop: 20, marginBottom: 20}}>

                    {TabButton(currentTab, setCurrentTab, "Редактировать профиль", 'person', setContent)}
                    {TabButton(currentTab, setCurrentTab, "Редактировать почту", 'mail', setContent)}
                    {TabButton(currentTab, setCurrentTab, "Сменить пароль", 'key', setContent)}

                </View>
                
                <View style={Settings.line}/>

                <View style={{ paddingLeft: 15 }}>
                    {TabButton(currentTab, setCurrentTab, "Назад", 'exit', setContent, navigation)}
                </View>

            </View>

            <Animated.View style={{
                flexGrow: 1,
                backgroundColor: 'white',
                position: 'absolute',
                top: 0,
                bottom: 0,
                left: 0,
                right: 0,
                paddingVertical: 20,
                borderRadius: showMenu ? 15 : 0,
                // Transforming View...
                transform: [
                { translateX: offsetValue }
                ]
            }}>

                <Animated.View style={{
                    width: '100%',
                    paddingTop: 30,
                    }}>
                    <TouchableOpacity 
                        style={Settings.driverContainer}
                        onPress={() => {
                        // Do Actions Here....
                        // Scaling the view...

                        Animated.timing(offsetValue, {
                        // YOur Random Value...
                        toValue: showMenu ? 0 : 230,
                        duration: 300,
                        useNativeDriver: true
                        })
                        .start()

                        setShowMenu(!showMenu);
                    }}>

                        <Ionicons name={'menu'} size={38} color={'#A7A7A7'} />
                        <Text style={Settings.title}>{currentTab}</Text>
                    
                    </TouchableOpacity>

                    {content}

                </Animated.View>

            </Animated.View>

        </View>
    );
}

// For multiple Buttons...
const TabButton = (currentTab, setCurrentTab, title, icon, setContent, navigation) => {
    return (

        <TouchableOpacity 
            onPress={() => {
                switch (title) {
                    case 'Редактировать профиль':
                        setCurrentTab(title);
                        setContent(change_profile);
                        break
                    case 'Редактировать почту':
                        setCurrentTab(title);
                        setContent(change_email);
                        break
                    case 'Сменить пароль':
                        setCurrentTab(title);
                        setContent(change_password);
                        break
                    case 'Назад':
                        navigation.goBack();
                        break
                        
                }

            }}
        >
            
            <View style={{
                flexDirection: "row",
                alignItems: 'center',
                paddingVertical: 8,
                paddingLeft: 10,
                paddingRight: 35,
                borderRadius: 8,
                marginTop: 15
            }}>
                <Ionicons name={icon} size={25} color={'#555555'} />

                <Text style={{
                fontSize: 20,
                width: 150,
                textAlignVertical: 'center',
                paddingLeft: 10,
                color: "#555555",
                }}>{title}</Text>

            </View>
        </TouchableOpacity>
    );
}
