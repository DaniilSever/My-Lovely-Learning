import AsyncStorage from '@react-native-async-storage/async-storage';
import axios from 'axios';
import React, { createContext, useState } from "react";
import { COURSE_URL } from '../config/config'

export const CourseContext = createContext();

export const CourseProvider = ({children}) => {
    const [courseInfo, setCourseInfo] = useState({});

    return (
        <CourseContext.Provider 
            value={{
                courseInfo,
            }}
        >{children}</CourseContext.Provider>
    );
    
};