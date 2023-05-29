import React, { useContext } from "react";
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';

// Screens
import { Login } from "./screens/Login";
import { Registration } from "./screens/Register";
import { Home } from "./screens/Home";
import { AuthContext } from "./context/AuthContext";

export function Navigation() {
    const Stack = createStackNavigator()
    const {userInfo} = useContext(AuthContext)

    return (
        <NavigationContainer>
            <Stack.Navigator>
                {userInfo.token ? 
                (
                    <>
                        <Stack.Screen name="Home" component={Home} options={{headerShown: false}}/>
                    </>
                )
                :
                (
                    <>
                        <Stack.Screen name="Login" component={Login} options={{headerShown: false}} />
                        <Stack.Screen name="Reg" component={Registration} options={{headerShown: false}}/>
                    </>
                )}
            </Stack.Navigator>
        </NavigationContainer>
    );
};