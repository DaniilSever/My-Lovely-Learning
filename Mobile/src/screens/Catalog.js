import React from 'react';
import { ScrollView, Text, TouchableOpacity } from "react-native";
import Ionicons from 'react-native-vector-icons/Ionicons';
import { Catalog } from '../../styles/style';

export function CatalogScreen() {
    return (
        <ScrollView style={Catalog.container}>
            {/* добавить цикл с выводом курсов */}
            <TouchableOpacity 
                style={Catalog.CourseCatalog}    
            >
                <Ionicons name={'arrow-forward-circle'} size={32} color={'#A7A7A7'} />
                <Text style={Catalog.Text}></Text>
            </TouchableOpacity>
        </ScrollView>
    );
};

