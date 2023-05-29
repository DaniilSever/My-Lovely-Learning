import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity} from "react-native";
import { Auth, Global } from '../../styles/style';

export function Login({navigation}) {
    const [email, setEmail] = useState(null)
    const [password, setPassword] = useState(null)

    return (
        <View style={Global.container}>
            <View style={Auth.container}>
                <View style={Auth.loginform}>
                    <TextInput 
                        style={Auth.input}
                        value={email}
                        placeholder='Введите почту'
                        onChangeText={text => setEmail(text)}
                    
                    />
                    <TextInput 
                        style={Auth.input}
                        value={password}
                        placeholder='Введите пароль'
                        onChangeText={text => setPassword(text)}
                    
                    />
                    <TouchableOpacity
                        style={Auth.button}
                        onPress={()=> {}}
                    >
                        <Text style={Auth.btntext}>Войти</Text>
                    </TouchableOpacity>
                </View>
                <View style={Auth.regcontainer} >
                    <Text style={Auth.text}>Нет аккаунта?</Text>
                    <TouchableOpacity
                        onPress={() => navigation.navigate('Reg')}
                    >
                        <Text style={Auth.text}>Зарегистрироваться</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    );
};

