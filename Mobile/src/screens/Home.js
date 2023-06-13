import React, { useContext, useEffect, useState } from 'react';
import { ScrollView, View, Text, TouchableOpacity } from "react-native";
import { Global, Home, Catalog } from '../../styles/style';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Ionicons from 'react-native-vector-icons/Ionicons';

import { CourceScreen } from './Courses/Cource-Info';
import { CourseContext } from '../context/CourseContext';


export function HomeScreen({navigation}) {
    const {get_course, courseInfo} = useContext(CourseContext)

    useEffect(() => {
        get_course()
    }, []);

    return (
        <View style={Global.container}>
            <View style={Home.container}>
                <ScrollView style={Catalog.container}>
                    <TouchableOpacity 
                        style={Catalog.CourseCatalog}
                        onPress={() => {
                            navigation.navigate("Курс")
                        }}
                    >
                        <Ionicons name={'arrow-forward-circle'} size={32} color={'#A7A7A7'} />
                        <Text style={Catalog.Text}>{courseInfo.title}</Text>
                    </TouchableOpacity>
                </ScrollView>
            </View>
        </View>
    );
};


