import { useRef, useState } from 'react';
import { StatusBar } from 'expo-status-bar';
import { Animated, Image, Button, StyleSheet, Text, TouchableOpacity, View } from 'react-native';
import { gStyle, StyleProfile } from '../styles/style';

// Images
import menu from '../assets/appAssets/burger.png'
import close from '../assets/appAssets/close.png'

export default function Profile({ navigation }) {
  const [currentTab, setCurrentTab] = useState("Профиль");
  const [showMenu, setShowMenu] = useState(false);

  const offsetValue = useRef(new Animated.Value(0)).current;
  const closeButtonOffset = useRef(new Animated.Value(0)).current;
    return (
      <View style={gStyle.container}>
        {/* DriverLayout */}
        <View style={StyleProfile.Menu}>

          <Text style={(gStyle.text, StyleProfile.titleText)}>Меню</Text>

          <View style={{ marginTop: 50, marginLeft: 30 }}>
            {
              // Tab Bar Buttons....
            }

            {TabButton(currentTab, setCurrentTab, "Профиль")}
            {TabButton(currentTab, setCurrentTab, "Сертификаты")}
            <TouchableOpacity
              style={{ marginBottom: 50 }}
              onPress={() => navigation.navigate('Settings')}
            >
              <Text style={StyleProfile.ButtonText}>Настройки</Text>
            </TouchableOpacity>

          </View>

          <View style={{ marginLeft: 30 }}>
            {TabButton(currentTab, setCurrentTab, "Выход")}
          </View>

      </View>

      {/* Main */}
      <Animated.View style={{
        backgroundColor: 'white',
        position: 'absolute',
        paddingVertical: 50,
        paddingHorizontal: 15,
        top: 0,
        bottom: 0,
        left: 0,
        right: 0,
        borderRadius: showMenu ? 15 : 0,
        // Transforming View...
        transform: [
          { translateX: offsetValue }
        ]
      }}>

        {/* Header Profile */}
        <Animated.View style={{
          flexDirection: "row",
          alignItems: 'center',
          transform: [{
            translateY: closeButtonOffset
          }]
        }}>
          <TouchableOpacity 
          style={StyleProfile.driverButton}
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

            <Image source={showMenu ? close : menu} style={{
              width: 20,
              height: 20,
              tintColor: 'black',

            }}></Image>

          </TouchableOpacity>

          <Text style={{
              fontSize: 30,
              fontWeight: 'bold',
              color: 'black',
            }}>{currentTab}</Text>

        </Animated.View>

        {/* Main Content */}

        <View>
        </View>

      </Animated.View>

        <StatusBar style="auto" />
      </View>
    );
}

const TabButton = (currentTab, setCurrentTab, title) => {
  return (
    <TouchableOpacity onPress={() => {
      if (title == "Выход") {
        // Do your Stuff...
      } else {
        setCurrentTab(title)
      }
    }}>
      <View style={StyleProfile.ButtonMenu}>
        <Text style={(gStyle.text, StyleProfile.ButtonText)}>{title}</Text>
      </View>
    </TouchableOpacity>
  );
}