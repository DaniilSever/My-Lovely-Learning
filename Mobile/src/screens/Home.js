import React from 'react';
import { View, Text } from "react-native";
import { Global, Home } from '../../styles/style';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Catalog
import { CatalogScreen } from './Catalog';
import { CourceScreen } from './Courses/Cource-Info';

export function HomeScreen({navigation}) {
    const Stack = createStackNavigator()
    return (
        <View style={Global.container}>
            <View style={Home.container}>
                <CatalogScreenr/>
            </View>
        </View>
    );
};


