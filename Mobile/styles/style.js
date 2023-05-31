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

export const Home = StyleSheet.create({
    container: {
        paddingTop: 50,
    }, 
});

export const Catalog = StyleSheet.create({
    container: {
        flexDirection: "column",
        height: '100%',
    },

    CourseCatalog: {
        width: '100%',
        height: 50,
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: 15,
        backgroundColor: '#E9E9E9',
        borderColor: '#A7A7A7',
        borderWidth: 1,
        borderRadius: 30,
        marginBottom: 10,
    },

    text: {

    },

});

export const Profile = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#E9E9E9',
    },

    title: {
        fontSize: 22,
        textAlign: "center",
        color: "#555555",
        fontWeight: "bold",
    },

    driverContainer: {
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: 15,
        height: 50,
        width: 200,
    }, 

    menuBTN: {
        flexDirection: "row",

    },

    menuContainer: {
        paddingTop: 50,
    }, 

    line: {
        width: '100%',
        height: 1,
        backgroundColor: "#555555",
    },

    menuTitle: {
        paddingLeft: 15,
        fontSize: 26,
        fontWeight: "bold",
        color: '#555555',
    },
});

export const ScreenProfile = StyleSheet.create({
    container: {
        paddingTop: 25,
    },

    activeContainer: {
        flexDirection: "column",
        height: '100%',
    },

    CourseActive: {
        width: '100%',
        height: 50,
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: 15,
        backgroundColor: '#E9E9E9',
        borderColor: '#A7A7A7',
        borderWidth: 1,
        borderRadius: 30,
        marginBottom: 10,
    },

    certContainer: {
        flexDirection: "column",
        height: '100%',
    },

    CourseCert: {
        width: '100%',
        height: 50,
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: 15,
        backgroundColor: '#E9E9E9',
        borderColor: '#A7A7A7',
        borderWidth: 1,
        borderRadius: 30,
        marginBottom: 10,
    },

    Text: {

    },

    favoriteContainer: {
        flexDirection: "column",
        height: '100%',
    },

    CourseFavorite: {
        width: '100%',
        height: 50,
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: 15,
        backgroundColor: '#E9E9E9',
        borderColor: '#A7A7A7',
        borderWidth: 1,
        borderRadius: 30,
        marginBottom: 10,
    },
});

export const Settings = StyleSheet.create({
    container: {
        flex: 1,
        backgroundColor: '#E9E9E9',
    },

    title: {
        fontSize: 22,
        textAlign: "center",
        color: "#555555",
        fontWeight: "bold",
    },

    driverContainer: {
        flexDirection: "row",
        alignItems: "center",
        paddingLeft: 15,
        height: 50,
        width: 300,
    }, 

    menuBTN: {
        flexDirection: "row",

    },

    menuContainer: {
        paddingTop: 50,
    }, 

    line: {
        width: '100%',
        height: 1,
        backgroundColor: "#555555",
    },

    menuTitle: {
        paddingLeft: 15,
        fontSize: 26,
        fontWeight: "bold",
        color: '#555555',
    },
});

export const ScreenSettings = StyleSheet.create({
    container: {
        paddingTop: 25,
    },

    changeContainer: {
        flexDirection: "column",
        height: '100%',
        alignItems: 'center',
    }, 

    viewEmail: {
        width: '100%',
        height: 40,
        borderColor: "#A7A7A7",
        borderRadius: 30,
        marginBottom: 40,
        backgroundColor: "#E9E9E9",
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

    submitBTN: {
        width: 150,
        height: 50,
        backgroundColor: '#004E85',
        borderRadius: 30,
        alignItems: "center",
        justifyContent: "center",
    },

    btntext: {
        color: "#fff",
        fontSize: 16,
    },
});