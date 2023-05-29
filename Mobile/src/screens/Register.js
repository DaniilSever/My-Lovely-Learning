import React, { useState } from 'react';
import { View, Text, TextInput, TouchableOpacity} from "react-native";
import { Global, Register } from '../../styles/style';

export function Reg({navigation}) {
    const [username, setUsername] = useState(null)
    const [email, setEmail] = useState(null)
    const [password, setPassword] = useState(null)

    return (
        <View style={Global.container}>
            <View style={Register.container}>
                <View style={Register.registerform}>
                    <TextInput
                        style={Register.input}
                        value={username}
                        placeholder='Введите логин'
                        onChangeText={text => setUsername(text)}
                    />
                    <TextInput 
                        style={Register.input}
                        value={email}
                        placeholder='Введите почту'
                        onChangeText={text => setEmail(text)}
                    
                    />
                    <TextInput 
                        style={Register.input}
                        value={password}
                        placeholder='Введите пароль'
                        onChangeText={text => setPassword(text)}
                    
                    />
                    <TouchableOpacity
                        style={Register.button}
                        onPress={()=> {}}
                    >
                        <Text style={Register.btntext}>Зарегистрироваться</Text>
                    </TouchableOpacity>
                </View>
                <View style={Register.logincontainer} >
                    <Text style={Register.text}>Есть аккаунт?</Text>
                    <TouchableOpacity
                        onPress={() => navigation.navigate('Login')}
                    >
                        <Text style={Register.text}>Войти</Text>
                    </TouchableOpacity>
                </View>
            </View>
        </View>
    );
};

