import * as React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createBottomTabNavigator } from '@react-navigation/bottom-tabs';
import { createNativeStackNavigator } from '@react-navigation/native-stack';

import Ionicons from 'react-native-vector-icons/Ionicons';

// Screens

import Catalog from './components/Catalog'
import Profile from './components/Profile'
import Settings from './components/Settings'

// Cources

import Course from './components/Cource/Cource_1';

function HomeScreen() {
  const Stack = createNativeStackNavigator();
  return (
    <Stack.Navigator>
      <Stack.Screen name='Catalog' component={Catalog} options={{headerShown: false}}/>
      <Stack.Screen name='Course' component={Course} />
    </Stack.Navigator>
  );
}

function PofileScreen() {
  const Stack = createNativeStackNavigator();
  return (
    <Stack.Navigator>
      <Stack.Screen name="Profile" component={Profile} options={{headerShown: false}}/>
      <Stack.Screen name="Settings" component={Settings}/>
    </Stack.Navigator>
  );
}

export default function App() {
  const Tab = createBottomTabNavigator();

  return (
    <NavigationContainer>
      <Tab.Navigator
        screenOptions={({ route }) => ({
          tabBarIcon: ({ focused, color, size }) => {
            let iconName;

            if (route.name === 'Catalog') {
              iconName = focused
                ? 'ios-information-circle'
                : 'ios-information-circle-outline';
            } else if (route.name === 'Profile') {
              iconName = focused ? 'ios-list' : 'ios-list-outline';
            }

            // You can return any component that you like here!
            return <Ionicons name={iconName} size={size} color={color} />;
          },
          tabBarActiveTintColor: 'tomato',
          tabBarInactiveTintColor: 'gray',
        })}
      >
        <Tab.Screen name="Catalog" component={HomeScreen} options={{headerShown: false}}/>
        <Tab.Screen name="Profile" component={PofileScreen} options={{headerShown: false}}/>
      </Tab.Navigator>
    </NavigationContainer>
  );
}
