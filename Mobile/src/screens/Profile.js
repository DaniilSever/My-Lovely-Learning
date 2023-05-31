import React, { useState, useRef } from 'react';
import { View, Text, StyleSheet, TouchableOpacity, Animated} from "react-native";
import Ionicons from 'react-native-vector-icons/Ionicons';
import { Profile } from '../../styles/style';

// content
import { profile, cert, favorite } from './ScreenProfile';


export function ProfileScreen({navigation}) {
    const [currentTab, setCurrentTab] = useState("Профиль");
    // To get the curretn Status of menu ...
    const [showMenu, setShowMenu] = useState(false);
    const [content, setContent] = useState(profile)


    const offsetValue = useRef(new Animated.Value(0)).current;

    return (
        <View style={Profile.container}>
            <View style={Profile.menuContainer}>

                <Text style={Profile.menuTitle}>
                    Меню
                </Text>

                <View style={{ paddingLeft: 15, marginTop: 20, marginBottom: 20}}>

                    {TabButton(currentTab, setCurrentTab, "Профиль", 'home', setContent)}
                    {TabButton(currentTab, setCurrentTab, "Сертификаты", 'school', setContent)}
                    {TabButton(currentTab, setCurrentTab, "Избранные", 'bookmark', setContent)}
                    {TabButton(currentTab, setCurrentTab, "Настройки", 'flower', setContent, navigation)}

                </View>
                
                <View style={Profile.line}/>

                <View style={{ paddingLeft: 15 }}>
                    {TabButton(currentTab, setCurrentTab, "Выход", 'exit')}
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
                        style={Profile.driverContainer}
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
                        <Text style={Profile.title}>{currentTab}</Text>
                    
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
                    case 'Профиль':
                        setCurrentTab(title);
                        setContent(profile);
                        break
                    case 'Сертификаты':
                        setCurrentTab(title);
                        setContent(cert);
                        break
                    case 'Избранные':
                        setCurrentTab(title);
                        setContent(favorite);
                        break
                    case 'Настройки':
                        navigation.navigate('Settings');
                        break
                    case 'Назад':
                        break
                        
                }

            }}
        >
            
            <View style={{
                flexDirection: "row",
                alignItems: 'center',
                paddingVertical: 8,
                paddingLeft: 13,
                paddingRight: 35,
                borderRadius: 8,
                marginTop: 15
            }}>
                <Ionicons name={icon} size={25} color={'#555555'} />

                <Text style={{
                fontSize: 20,
                paddingLeft: 15,
                textAlignVertical: 'center',
                color: "#555555",
                }}>{title}</Text>

            </View>
        </TouchableOpacity>
    );
}

