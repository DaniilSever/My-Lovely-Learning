import React from 'react';
import { View, Text } from "react-native";
import { Global, Home } from '../../styles/style';


export function profile() {
    return (
        <View style={Global.container}>
            <View>
                <Text>Профиль</Text>
            </View>
        </View>
    );
};



export function cert() {
    return (
        <View style={Global.container}>
            <View>
                <Text>Сертификаты</Text>
            </View>
        </View>
    );
};

export function favorite() {
    return (
        <View style={Global.container}>
            <View>
                <Text>Избранные</Text>
            </View>
        </View>
    );
};




