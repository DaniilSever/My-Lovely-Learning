import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Text, View } from 'react-native';
import { gStyle } from '../styles/style';


export default function Catalog({ navigation }) {
    return (
      <View style={gStyle.container}>
        <Text>Catalog</Text>
        <Button 
          title="Course"
          onPress={() => navigation.navigate('Course')}
        />
        <StatusBar style="auto" />
      </View>
    );
}