import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import { gStyle } from '../styles/style';

export default function Profile({ navigation }) {
    return (
      <View style={gStyle.container}>
        <Text>Profile</Text>
        <Button 
          title="Settings"
          onPress={() => navigation.navigate('Settings')}
        />
        <StatusBar style="auto" />
      </View>
    );
}