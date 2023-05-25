import React, { useContext, useState } from "react";
import { Button, Text, TextInput, TouchableOpacity, View } from "react-native";
import { StyleLogin, gStyle } from "../styles/style";
import { AuthContext } from "./context/AuthContext";

export function Login() {
    
    const [email, setEmail] = useState(null);
    const [password, setPassword] = useState(null);
    const val = useContext(AuthContext)

    return (
        <View style={gStyle.container}>
            <View style={StyleLogin.container}>
                <Text> {val} </Text>
                <View style={StyleLogin.loginForm}>
                    <TextInput 
                        style={StyleLogin.input} 
                        placeholder="Введите почту"
                        onChangeText={text => setEmail(text)}
                    />
                    <TextInput 
                        style={StyleLogin.input} 
                        placeholder="Введите пароль"
                        onChangeText={text => setPassword(text)}
                    />
                    <TouchableOpacity 
                        style={StyleLogin.submitBTN}
                        onPress={() => {}}
                    >
                        <Text style={StyleLogin.submitText}>Войти</Text>
                    </TouchableOpacity>
                </View>
                
                <View style={StyleLogin.regForm}>
                    <Text>Нет аккаунта?</Text>
                    <TouchableOpacity
                        onPress={() => {}}
                    >
                        <Text>Зарегистрироваться</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    );
};