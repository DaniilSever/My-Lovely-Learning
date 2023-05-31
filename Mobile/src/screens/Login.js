import React, { useContext, useState } from 'react';
import { View, Text, TextInput, TouchableOpacity} from "react-native";
import { Auth, Global } from '../../styles/style';
import { AuthContext } from '../context/AuthContext';
import Spinner from 'react-native-loading-spinner-overlay';

export function Login({navigation}) {
    const [username, setUsername] = useState(null);
    const [password, setPassword] = useState(null)

    const {isLoading, login} = useContext(AuthContext)

    return (
        <View style={Global.container}>
            <Spinner visible={isLoading} />
            <View style={Auth.container}>
                <View style={Auth.loginform}>
                    <TextInput 
                        style={Auth.input}
                        value={username}
                        placeholder='Введите почту'
                        onChangeText={text => setUsername(text)}
                    
                    />
                    <TextInput 
                        style={Auth.input}
                        value={password}
                        placeholder='Введите пароль'
                        onChangeText={text => setPassword(text)}
                    
                    />
                    <TouchableOpacity
                        style={Auth.button}
                        onPress={()=> {
                            login(username, password)
                        }}
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

