import React from "react";
import { StyleSheet } from "react-native";

export const Global = StyleSheet.create({
    container: {
        height: '100%',
        width: '100%',
        paddingHorizontal: 15,
    },

    center: {
        alignItems: "center",
        justifyContent: "center",
    }, 
    
    text: {
        fontSize: 20,
    },
});

export const Auth = StyleSheet.create({
    container: {
        width: '100%',
        height: '100%',
        justifyContent: "center",
    },

    loginform: {
        alignItems: "center",
        justifyContent: "center",
        marginBottom: 20,
    },
    
    input: {
        width: '100%',
        height: 50,
        backgroundColor: '#DFDFDF',
        borderColor: '#A7A7A7',
        borderRadius: 30,
        paddingLeft: 25,
        borderWidth: 1,
        marginBottom: 20,
        
        fontSize: 16,
    },

    button: {
        width: 150,
        height: 50,
        backgroundColor: '#004E85',
        borderRadius: 30,
        alignItems: "center",
        justifyContent: "center",
    },

    btntext: {
        color: "#fff",
        fontSize: 18,
    },

    regcontainer: {
        flexDirection: "row",
        justifyContent: "center",
    },

    text: {
        fontSize: 16,
    }
});

export const Register = StyleSheet.create({
    container: {
        width: '100%',
        height: '100%',
        justifyContent: "center",
    },

    registerform: {
        alignItems: "center",
        justifyContent: "center",
        marginBottom: 20,
    },
    
    input: {
        width: '100%',
        height: 50,
        backgroundColor: '#DFDFDF',
        borderColor: '#A7A7A7',
        borderRadius: 30,
        paddingLeft: 25,
        borderWidth: 1,
        marginBottom: 20,
        
        fontSize: 16,
    },

    button: {
        width: 250,
        height: 50,
        backgroundColor: '#004E85',
        borderRadius: 30,
        alignItems: "center",
        justifyContent: "center",
    },

    btntext: {
        color: "#fff",
        fontSize: 18,
    },

    logincontainer: {
        flexDirection: "row",
        justifyContent: "center",
    },

    text: {
        fontSize: 16,
    }
});