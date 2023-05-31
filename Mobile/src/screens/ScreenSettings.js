import React from 'react';
import { View, Text, ScrollView, TouchableOpacity, TextInput} from "react-native";
import { Global, ScreenSettings } from '../../styles/style';
import Ionicons from 'react-native-vector-icons/Ionicons';

export function change_profile() {
    return (
        <View style={Global.container}>
            <View style={ScreenSettings.container}>
                <ScrollView contentContainerStyle={ScreenSettings.changeContainer}>
                    
                    <TextInput
                        style={ScreenSettings.input}
                        placeholder='Введите Никнейм'
                    />
                    
                    <TouchableOpacity
                        style={ScreenSettings.submitBTN}
                        onPress={() => {

                        }}
                    >
                        <Text style={ScreenSettings.btntext}>
                            Редактировать
                        </Text>
                    </TouchableOpacity>


                </ScrollView>
            </View>
        </View>
    );
};

export function change_email() {
    return (
        <View style={Global.container}>
            <View style={ScreenSettings.container}>
                <ScrollView contentContainerStyle={ScreenSettings.changeContainer}>
                    <View style={ScreenSettings.viewEmail}>
                        {/* добавить отображвение почты */}
                    </View>
                    
                    <TextInput
                        style={ScreenSettings.input}
                        placeholder='Введите почту'
                    />
                    
                    <TouchableOpacity
                        style={ScreenSettings.submitBTN}
                        onPress={() => {

                        }}
                    >
                        <Text style={ScreenSettings.btntext}>
                            Добавить почту
                        </Text>
                    </TouchableOpacity>

                </ScrollView>
            </View>
        </View>
    );
};

export function change_password() {
    return (
        <View style={Global.container}>
            <View style={ScreenSettings.container}>
                <ScrollView contentContainerStyle={ScreenSettings.changeContainer}>
                    <TextInput
                        style={ScreenSettings.input}
                        placeholder='Введите старый пароль'
                    />
                    <TextInput
                        style={ScreenSettings.input}
                        placeholder='Введите новый пароль'
                    />
                    
                    <TextInput
                        style={ScreenSettings.input}
                        placeholder='Подтвердите новый пароль'
                    />
                    
                    
                    <TouchableOpacity
                        style={ScreenSettings.submitBTN}
                        onPress={() => {

                        }}
                    >
                        <Text style={ScreenSettings.btntext}>
                            Сменить пароль
                        </Text>
                    </TouchableOpacity>

                </ScrollView>
            </View>
        </View>
    );
};




