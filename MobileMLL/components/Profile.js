import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { gStyle } from '../styles/style';

export default function Catalog() {
    return (
      <View style={gStyle.container}>
        <Text>Profile</Text>
        <StatusBar style="auto" />
      </View>
    );
}