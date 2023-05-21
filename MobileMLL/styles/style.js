import { StyleSheet } from "react-native";

export const gStyle = StyleSheet.create({
    container: {
        width: '100%',
        height: '100%',
        paddingTop: 50,
        padding: (10,10),
        paddingBottom: 20,
    },
});

export const StyleCatalog = StyleSheet.create({
    container: {
        height: '8%',
        borderWidth: 1,
        justifyContent: "center",
        borderRadius: 30,
        borderColor: '#A7A7A7',
        backgroundColor: '#E9E9E9',
    },

    insideContainer: {
        width: '100%',
        height: '100%',
        justifyContent: "center",
    },

    textCatalog: {

    },
});

export const StyleProfile = StyleSheet.create({
    container: {},
    driverContainer: {
        zIndex: 10,
        width: '40%',
        height: '100%',
        padding: (0,20,20,20),
        backgroundColor: '#DFDFDF',
    },
    titleText: {
        fontSize: 30,
        fontWeight: "bold",
    },

    Menu: {
        justifyContent: "flex-start",
        padding: 5,
    },

    driverButton: {
        width: 30,
        height: 30,
        tintColor: 'black',
        justifyContent: "center",
    },
    ButtonMenu: {
        marginBottom: 20,
    },
    ButtonText: {
        fontSize: 20,
    }
});

export const StyleLogin = StyleSheet.create({
    container: { 
        paddingTop: '60%',
    },
    input: {
        width: '100%',
        height: 45,
        borderWidth: 1,
        justifyContent: "center",
        borderRadius: 30,
        marginBottom: 30,
        borderColor: '#A7A7A7',
        backgroundColor: '#E9E9E9',
        textAlign: "center",
    },
    loginForm: {
        alignItems: "center",
    },
    regForm: {
        flexDirection: 'row',
        justifyContent: "center",
    },
    submitBTN: {
        width: '30%',
        height: '20%',
        backgroundColor: '#004E85',
        alignItems: "center",
        justifyContent: "center",
        borderRadius: 30,
    },
    submitText: {
        color: '#FFFFFF'
    }
});