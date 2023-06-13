import React from 'react';
import { ScrollView, View, Text, TouchableOpacity } from "react-native";
import { Global, Home, Catalog } from '../../styles/style';
import Ionicons from 'react-native-vector-icons/Ionicons';

export function HomeScreen({navigation}) {
    return (
        <View style={Global.container}>
            <View style={Home.container}>
                <ScrollView style={Catalog.container}>
                {/* добавить цикл с выводом курсов */}
                <TouchableOpacity 
                    style={Catalog.CourseCatalog}
                    onPress={() => {
                        navigation.navigate("Course")
                    }}
                >
                    <Ionicons name={'arrow-forward-circle'} size={32} color={'#A7A7A7'} />
                    <Text style={Catalog.Text}></Text>
                </TouchableOpacity>
            </ScrollView>
            </View>
        </View>
    );
};


