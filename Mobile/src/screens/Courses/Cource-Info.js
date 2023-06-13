import React, { useContext } from 'react';
import { View, Text, Image, ScrollView, TouchableOpacity } from "react-native";
import { Global, Course } from '../../../styles/style';
import { CourseContext } from '../../context/CourseContext';

// Screen


export function CourceScreen({navigation}) {
    const {courseInfo} = useContext(CourseContext)
    return (
        <View style={Global.container}>
            <ScrollView style={Course.container}>
                <Text style={Course.title}>{courseInfo.title}</Text>
                <Text style={Course.description}>{courseInfo.description}</Text>
                {/* <View style={Course.btncontainer}>
                    <TouchableOpacity
                        style={Course.btnback}
                        onPress={()=>{navigation.goBack();}}
                    >
                        <Text style={Course.btntext}>Назад</Text>
                    </TouchableOpacity>
                    <TouchableOpacity
                        style={Course.btn}
                        onPress={()=>{}}
                    >
                        <Text style={Course.btntext}>Записаться</Text>
                    </TouchableOpacity>
                </View> */}
            </ScrollView>
        </View>
    );
};


