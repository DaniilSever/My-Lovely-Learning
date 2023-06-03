import React from 'react';
import { View, Text, ScrollView, TouchableOpacity} from "react-native";
import { Global, ScreenProfile } from '../../styles/style';
import Ionicons from 'react-native-vector-icons/Ionicons';
import { AuthContext } from '../context/AuthContext';

export function profile() {
    return (
        <View style={Global.container}>
            <View style={ScreenProfile.container}>
                <ScrollView style={ScreenProfile.activeContainer}>
                    {/* добавить цикл с выводом курсов */}
                    <TouchableOpacity 
                        style={ScreenProfile.CourseActive}    
                    >
                        <Ionicons name={'arrow-forward-circle'} size={32} color={'#004E85'} />
                        <Text style={ScreenProfile.Text}></Text>
                    </TouchableOpacity>
                </ScrollView>
            </View>
        </View>
    );
};

export function cert() {
    return (
        <View style={Global.container}>
            <View style={ScreenProfile.container}>
                <ScrollView style={ScreenProfile.certContainer}>
                    {/* добавить цикл с выводом курсов */}
                    <TouchableOpacity 
                        style={ScreenProfile.CourseCert}    
                    >
                        <Ionicons name={'code-slash'} size={32} color={'#004E85'} />
                        <Text style={ScreenProfile.Text}></Text>
                    </TouchableOpacity>
                </ScrollView>
            </View>
        </View>
    );
};

export function favorite() {
    return (
        <View style={Global.container}>
            <View style={ScreenProfile.container}>
                <ScrollView style={ScreenProfile.favoriteContainer}>
                    {/* добавить цикл с выводом курсов */}
                    <TouchableOpacity 
                        style={ScreenProfile.CourseFavorite}    
                    >
                        <Ionicons name={'star'} size={32} color={'#004E85'} />
                        <Text style={ScreenProfile.Text}></Text>
                    </TouchableOpacity>
                </ScrollView>
            </View>
        </View>
    );
};




