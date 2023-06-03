import React, { useContext } from "react";
import { AuthContext } from "./context/AuthContext";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import Ionicons from 'react-native-vector-icons/Ionicons';

// Screens
import { Login } from "./screens/Login";
import { Registration } from "./screens/Register";
import { HomeScreen } from "./screens/Home";
import { ProfileScreen } from "./screens/Profile"
import { SettingsScreen } from "./screens/Settings"
import { CourceScreen } from "./screens/Courses/Cource-Info";

export function Navigation() {
    const Stack = createStackNavigator()
    const {userInfo} = useContext(AuthContext)

    return (
        <NavigationContainer>
            <Stack.Navigator>
                {userInfo.token ? 
                (
                    <>
                        <Stack.Screen name="Start" component={TabNavigations} options={{headerShown: false}}/>
                        <Stack.Screen name="Settings" component={SettingsScreen} options={{headerShown: false}}/>
                    </>
                )
                :
                (
                    <>
                        <Stack.Screen name="Login" component={Login} options={{headerShown: false}} />
                        <Stack.Screen name="Reg" component={Registration} options={{headerShown: false}}/>
                    </>
                )}
            </Stack.Navigator>
        </NavigationContainer>
    );
};

function TabNavigations() {
    const Tab = createBottomTabNavigator();
    
    return (
        <Tab.Navigator
            screenOptions={({ route }) => ({
            tabBarIcon: ({ focused, color, size }) => {
                let iconName;

                if (route.name === 'Каталог') {
                iconName = focused
                    ? 'layers'
                    : 'layers-outline';
                } else if (route.name === 'Профиль') {
                iconName = focused ? 'home' : 'home-outline';
                }

                // You can return any component that you like here!
                return <Ionicons name={iconName} size={size} color={color} />;
            },
            tabBarActiveTintColor: '#004E85',
            tabBarInactiveTintColor: 'gray',
            tabBarLabelStyle: {
                fontSize: 16, 
            },
            })}
        >
        <Tab.Screen name="Каталог" component={HomeScreen} options={{headerShown: false}}/>
        <Tab.Screen name="Профиль" component={ProfileScreen} options={{headerShown: false}}/>
      </Tab.Navigator>
    );
};

function CatalogScreen() {
    const Stack = createStackNavigator()
    return (
        <Stack.Navigator>
            <Stack.Screen name="Catalog" component={CatalogScreen}/>
            <Stack.Screen name="Course" component={CourceScreen}/>
        </Stack.Navigator>
    );
};