import { StatusBar } from 'expo-status-bar';
import { Button, StyleSheet, Image, Text, TouchableOpacity, View } from 'react-native';

import { gStyle, StyleCatalog } from '../styles/style';


export default function Catalog({ navigation }) {
    return (
      <View style={gStyle.container}>
        <TouchableOpacity
          style={StyleCatalog.container}
          onPress={()=> navigation.navigate('Course')}>
            {/* ----------------Контайнер представления курса------------- */}
            <View style={StyleCatalog.insideContainer}>
              <Image
                // source={}
              />
              <Text style={StyleCatalog.textCatalog}></Text>
            </View>
            {/* ---------------------------------------------------------- */}
        </TouchableOpacity>
        <StatusBar style="auto" />
      </View>
    );
}