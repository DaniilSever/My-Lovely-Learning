import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import { gStyle } from '../../styles/style';


export default function Course() {
    return (
      <View style={gStyle.container}>
        <Text>Course</Text>
        <StatusBar style="auto" />
      </View>
    );
}