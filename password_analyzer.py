#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
محرك تحليل كلمات المرور لـ GuessPass
"""

import re
import random
import string
from datetime import datetime

class PasswordAnalyzer:
    def __init__(self):
        self.common_passwords = self.load_common_passwords()
        self.leet_subs = {
            'a': ['@', '4'],
            'e': ['3'],
            'i': ['1', '!'],
            'o': ['0'],
            's': ['5', '$'],
            't': ['7']
        }
        
        # أنماط الضعف الشائعة
        self.weak_patterns = [
            r'^\d+$',  # أرقام فقط
            r'^[a-zA-Z]+$',  # أحرف فقط
            r'^.+123$',  # تنتهي بـ 123
            r'^.+!$',  # تنتهي بـ !
        ]

    def load_common_passwords(self):
        """تحميل قائمة كلمات المرور الشائعة"""
        common_passwords = set([
            'password', '123456', '12345678', '1234', 'qwerty', '12345',
            'dragon', 'baseball', 'football', 'letmein', 'monkey',
            'abc123', 'master', 'hello', 'freedom', 'whatever',
            'qazwsx', 'password1', '123123', 'admin', 'welcome'
        ])
        
        # محاولة تحميل من ملف إذا وجد
        try:
            with open('common_passwords.txt', 'r', encoding='utf-8') as f:
                file_passwords = set(line.strip().lower() for line in f if line.strip())
                common_passwords.update(file_passwords)
        except FileNotFoundError:
            pass
        
        return common_passwords

    def generate_variations(self, base_string):
        """توليد أشكال مختلفة للنص"""
        variations = set()
        
        if not base_string or len(base_string) < 2:
            return variations
        
        # الأشكال الأساسية
        variations.add(base_string)
        variations.add(base_string.lower())
        variations.add(base_string.upper())
        variations.add(base_string.capitalize())
        
        # بدائل Leet Speak
        for char, subs in self.leet_subs.items():
            for sub in subs:
                leet_version = base_string.lower().replace(char, sub)
                variations.add(leet_version)
                
                # نسخ مع الحروف الكبيرة
                variations.add(leet_version.capitalize())
        
        return variations

    def generate_date_patterns(self, day, month, year):
        """توليد أنماط التواريخ"""
        patterns = set()
        
        if not all([day, month, year]):
            return patterns
        
        # تنسيقات التاريخ المختلفة
        date_combinations = [
            # يوم + شهر + سنة
            f"{day}{month}{year}",
            f"{day}{month}{year[2:]}",  # آخر سنتين من السنة
            
            # شهر + يوم + سنة
            f"{month}{day}{year}",
            f"{month}{day}{year[2:]}",
            
            # سنة + شهر + يوم
            f"{year}{month}{day}",
            f"{year[2:]}{month}{day}",
            
            # يوم + شهر
            f"{day}{month}",
            f"{month}{day}",
        ]
        
        patterns.update(date_combinations)
        return patterns

    def analyze_password_strength(self, password):
        """تحليل قوة كلمة المرور"""
        if not password:
            return {'score': 0, 'strength': 'unknown', 'feedback': ['The password is blank.']}
        
        score = 0
        feedback = []
        
        # الطول
        if len(password) >= 12:
            score += 2
        elif len(password) >= 8:
            score += 1
            feedback.append("Try a longer password (12 characters or more)")
        else:
            feedback.append("The password is very short (Minimum 8 characters)")
        
        # التنوع
        has_upper = bool(re.search(r'[A-Z]', password))
        has_lower = bool(re.search(r'[a-z]', password))
        has_digit = bool(re.search(r'\d', password))
        has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))
        
        char_types = sum([has_upper, has_lower, has_digit, has_special])
        
        if char_types >= 3:
            score += 2
        elif char_types >= 2:
            score += 1
            feedback.append("Add more character types (Large, small, numbers, symbols)")
        else:
            feedback.append("Use different types of letters")
        
        # الأنماط الضعيفة
        for pattern in self.weak_patterns:
            if re.match(pattern, password):
                score -= 1
                feedback.append("Avoid simple and predictable patterns")
                break
        
        # الكلمات الشائعة
        if password.lower() in self.common_passwords:
            score = 0
            feedback.append("This is a very common and insecure password.")
        
        # تحديد مستوى القوة
        if score >= 4:
            strength = "Very strong 🛡️"
        elif score >= 3:
            strength = "Strong ✅"
        elif score >= 2:
            strength = "Moderate ⚠️"
        elif score >= 1:
            strength = "Weak 🚨"
        else:
            strength = "Extremely dangerous 💀"
        
        return {
            'score': max(score, 0),
            'strength': strength,
            'feedback': feedback,
            'length': len(password),
            'has_upper': has_upper,
            'has_lower': has_lower,
            'has_digit': has_digit,
            'has_special': has_special
        }

    def generate_weak_passwords(self, user_data):
        """توليد كلمات مرور ضعيفة محتملة بناءً على المعلومات الشخصية"""
        weak_passwords = set()
        
        # معلومات المستخدم
        name = user_data.get('name', '')
        birth_year = user_data.get('birth_year', '')
        birth_month = user_data.get('birth_month', '')
        birth_day = user_data.get('birth_day', '')
        hobbies = user_data.get('hobbies', '')
        pet_name = user_data.get('pet_name', '')
        favorite_number = user_data.get('favorite_number', '')
        nickname = user_data.get('nickname', '')
        
        # توليد الاختلافات
        name_variations = self.generate_variations(name)
        nickname_variations = self.generate_variations(nickname)
        
        hobbies_variations = set()
        for hobby in hobbies.split(','):
            hobby_clean = hobby.strip()
            if hobby_clean:
                hobbies_variations.update(self.generate_variations(hobby_clean))
        
        pet_variations = self.generate_variations(pet_name)
        date_patterns = self.generate_date_patterns(birth_day, birth_month, birth_year)
        
        # اللواحق الشائعة
        common_suffixes = [
            '', '123', '1234', '12345', '!', '!!', '1', '12', 
            '2023', '2024', '2025', '00', '000', '0000', '007','top','100','100%','1020','1245678'
        ]
        
        # توليد المجموعات
        all_bases = name_variations | nickname_variations | hobbies_variations | pet_variations
        
        for base in all_bases:
            if base and len(base) >= 2:
                for suffix in common_suffixes:
                    # الأساس + اللاحقة
                    weak_passwords.add(base + suffix)
                    
                    # الأساس + التاريخ + اللاحقة
                    for date_pattern in date_patterns:
                        weak_passwords.add(base + date_pattern + suffix)
        
        # إضافة أنماط التاريخ بمفردها
        weak_passwords.update(date_patterns)
        
        # إضافة الرقم المفضل
        if favorite_number:
            for base in all_bases:
                weak_passwords.add(base + favorite_number)
            for date_pattern in date_patterns:
                weak_passwords.add(date_pattern + favorite_number)
        
        # إضافة المجموعات الخاصة
        special_combinations = [
            name + pet_name,
            nickname + birth_year,
            pet_name + birth_year[2:],
        ]
        
        for combo in special_combinations:
            if len(combo) >= 4:
                weak_passwords.add(combo)
        
        # تصفية وترتيب النتائج
        filtered_passwords = [
            pwd for pwd in weak_passwords 
            if 4 <= len(pwd) <= 30
        ]
        
        # إرجاع النتائج مرتبة حسب الطول
        return sorted(filtered_passwords, key=len)

    def generate_strong_password(self, length=16):
        """توليد كلمة مرور قوية"""
        if length < 8:
            length = 8
        
        # مجموعات الأحرف
        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'
        
        # التأكد من وجود حرف من كل نوع
        password = [
            random.choice(lowercase),
            random.choice(uppercase),
            random.choice(digits),
            random.choice(symbols)
        ]
        
        # إكمال الباقي عشوائياً
        all_chars = lowercase + uppercase + digits + symbols
        password.extend(random.choice(all_chars) for _ in range(length - 4))
        
        # خلط الأحرف
        random.shuffle(password)
        
        return ''.join(password)