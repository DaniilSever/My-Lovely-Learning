import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import React, { createContext, useState } from "react";
import {BASE_URL} from '../config/config'

export const AuthContext = createContext();

export const AuthProvider = ({children}) => {
    const [userInfo, setUserInfo] = useState({});
    const [isLoading, setIsLoading] = useState(false);

    const register = (username, email, password) => {
        setIsLoading(true)
        axios
            .post(`${BASE_URL}create/`, {
                username,
                email,
                password,
            })
            .then(res => {
                let userInfo = res.data;
                setUserInfo(userInfo);
                AsyncStorage.setItem('userInfo', JSON.stringify(userInfo));
                setIsLoading(false);
            })
            .catch(e => {
                console.log(`register error ${e}`);
                setIsLoading(false);
            });
    };

    const login = (username, password) => {
        setIsLoading(true);
    
        axios
            .post(`${BASE_URL}login/`, {
                username,
                password,
            })
            .then(res => {
                let userInfo = res.data;
                setUserInfo(userInfo);
                AsyncStorage.setItem('userInfo', JSON.stringify(userInfo));
                setIsLoading(false);
            })
            .catch(e => {
                console.log(`login error ${e}`);
                setIsLoading(false);
            });
    };

    return (
        <AuthContext.Provider value={{
            isLoading,
            userInfo,
            register,
            login,
        }}>{children}</AuthContext.Provider>
    );
    
};