import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import { gStyle } from '../styles/style';


export default function Settings() {
    return (
      <View style={gStyle.container}>
        <Text>Settings</Text>
        <StatusBar style="auto" />
      </View>
    );
}