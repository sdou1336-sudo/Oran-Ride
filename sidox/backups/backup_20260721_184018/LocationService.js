import React, { useEffect, useState } from 'react';
import { Platform, PermissionsAndroid, Alert } from 'react-native';
import Geolocation from '@react-native-community/geolocation';

// 1. طلب صلاحيات الـ GPS للهاتف
export const requestLocationPermission = async () => {
  if (Platform.OS === 'ios') return true;
  try {
    const granted = await PermissionsAndroid.request(
      PermissionsAndroid.PERMISSIONS.ACCESS_FINE_LOCATION
    );
    return granted === PermissionsAndroid.RESULTS.GRANTED;
  } catch (err) {
    console.warn(err);
    return false;
  }
};

// 2. جلب الموقع الحالي للمستخدم بدقة لربطه بالخريطة
export const getCurrentLocation = (onLocationSuccess, onLocationError) => {
  Geolocation.getCurrentPosition(
    (position) => {
      const { latitude, longitude } = position.coords;
      onLocationSuccess({ latitude, longitude });
    },
    (error) => {
      Alert.alert("خطأ في تحديد الموقع", error.message);
      onLocationError(error);
    },
    { enableHighAccuracy: true, timeout: 15000, maximumAge: 10000 }
  );
};

// 3. تتبع حركة السائق أو الراكب بشكل حي ومستمر
export const watchUserLocation = (onLocationUpdate) => {
  return Geolocation.watchPosition(
    (position) => {
      const { latitude, longitude } = position.coords;
      onLocationUpdate({ latitude, longitude });
    },
    (error) => console.log(error),
    { enableHighAccuracy: true, distanceFilter: 10 } // يحدّث الموقع كل 10 أمتار حركة
  );
};

