import React from 'react';
import { View, Text } from "react-native";
import { Global, Home } from '../../styles/style';

// Catalog
import { CatalogScreen } from './Catalog';

export function HomeScreen() {
    return (
        <View style={Global.container}>
            <View style={Home.container}>
                <CatalogScreen/>
            </View>
        </View>
    );
};


