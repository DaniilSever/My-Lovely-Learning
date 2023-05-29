import 'react-native-gesture-handler';
import React from 'react';
import { Navigation } from './src/navigations';
import { AuthProvider } from './src/context/AuthContext'

export default function App() {
  return (
    <AuthProvider>
       <Navigation/>
    </AuthProvider>
  );
};

