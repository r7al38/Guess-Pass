#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
GuessPass - Terminal Password Insight Generator
Developer : Mustafa Rahal
"""

import os
import sys
import time
import random
from datetime import datetime

# Adding the current path for importing modules
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from password_analyzer import PasswordAnalyzer

class Colors:
    """colors"""
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class GuessPass:
    def __init__(self):
        self.analyzer = PasswordAnalyzer()
        self.colors = Colors()
        
    def clear_screen(self):
        """clear terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')
    
    def print_banner(self):
        
        banner = f"""
{self.colors.CYAN}{self.colors.BOLD}
 ╔═══════════════════════════════════════╗
 ║  ██████╗  ██╗   ██╗ ███████╗ ███████╗ ║
 ║ ██╔════╝  ██║   ██║ ██╔════╝ ██╔════╝ ║
 ║ ██║  ███╗ ██║   ██║ ███████╗ ███████╗ ║
 ║ ██║   ██║ ██║   ██║ ╚════██║ ╚════██║ ║
 ║ ╚██████╔╝ ╚██████╔╝ ███████║ ███████║ ║
 ║  ╚═════╝   ╚═════╝  ╚══════╝ ╚══════╝ ║
 ║  ██████╗   ███████  ███████╗ ███████╗ ║
 ║  ██╔═══██  ██╔══██╗ ██╔════╝ ██╔════╝ ║
 ║  ██████╔╝  ███████║ ███████╗ ███████╗ ║
 ║  ██╔═══╝   ██╔══██║ ╚════██║ ╚════██║ ║
 ║  ██║       ██║  ██║ ███████║ ███████║ ║
 ║  ╚═╝       ╚═╝  ╚═╝ ╚══════╝ ╚══════╝ ║
 ╚═══════════════════════════════════════╝
{self.colors.RESET}
{self.colors.YELLOW}╔══════════════════════════════════════════════════════════════╗
{self.colors.YELLOW}║{self.colors.GREEN}           GuessPass - Terminal Password Analyzer         {self.colors.YELLOW}║
{self.colors.YELLOW}║{self.colors.CYAN}         Developed by: {self.colors.MAGENTA}r7al38{self.colors.CYAN} - Version 1.0           {self.colors.YELLOW}║
{self.colors.YELLOW}╚══════════════════════════════════════════════════════════════╝
{self.colors.RESET}
"""
        print(banner)
    
    def print_section(self, title, color=Colors.CYAN):
        """Show section with title"""
        width = 60
        print(f"\n{color}{self.colors.BOLD}╔{'═' * (width - 2)}╗{self.colors.RESET}")
        print(f"{color}{self.colors.BOLD}║ {title:<56} ║{self.colors.RESET}")
        print(f"{color}{self.colors.BOLD}╚{'═' * (width - 2)}╝{self.colors.RESET}")
    
    def get_user_input(self, prompt, required=False, input_type="text"):
        """Obtaining user input"""
        while True:
            try:
                if input_type == "text":
                    user_input = input(f"{self.colors.BLUE}[?] {prompt}: {self.colors.RESET}").strip()
                elif input_type == "number":
                    user_input = input(f"{self.colors.BLUE}[?] {prompt}: {self.colors.RESET}").strip()
                
                if required and not user_input:
                    print(f"{self.colors.RED}[!] هذا الحقل مطلوب{self.colors.RESET}")
                    continue
                
                return user_input
            except KeyboardInterrupt:
                self.exit_tool()
            except Exception as e:
                print(f"{self.colors.RED}[!] خطأ في الإدخال: {e}{self.colors.RESET}")
    
    def collect_user_data(self):
        """Collecting user data"""
        self.print_section("Collection of personal information", Colors.GREEN)
        
        user_data = {}
        
        print(f"\n{self.colors.YELLOW}[i] Enter personal information to analyze potential passwords{self.colors.RESET}")
        print(f"{self.colors.YELLOW}[i] Press Ctrl+C to exit at any time{self.colors.RESET}\n")
        
        # Basic Information
        user_data['name'] = self.get_user_input("full name", required=True)
        user_data['birth_year'] = self.get_user_input("Year of birth (ex: 1990)", input_type="number")
        user_data['birth_month'] = self.get_user_input("month of birth (1-12)", input_type="number")
        user_data['birth_day'] = self.get_user_input("birthday (1-31)", input_type="number")
        
        # Additional information
        user_data['hobbies'] = self.get_user_input("Hobbies (separated by a comma)", required=False)
        user_data['pet_name'] = self.get_user_input("pet name", required=False)
        user_data['favorite_number'] = self.get_user_input("favorite number", required=False)
        user_data['nickname'] = self.get_user_input("nickname", required=False)
        
        return user_data
    
    def validate_data(self, user_data):
        """Data verification"""
        # Check date of birth
        if user_data['birth_year'] and user_data['birth_month'] and user_data['birth_day']:
            try:
                birth_date = datetime(
                    int(user_data['birth_year']),
                    int(user_data['birth_month']),
                    int(user_data['birth_day'])
                )
                age = datetime.now().year - birth_date.year
                if age < 5 or age > 120:
                    print(f"{self.colors.RED}[!] Warning: Age is illogical{self.colors.RESET}")
            except ValueError:
                print(f"{self.colors.RED}[!] Warning: Incorrect date of birth{self.colors.RESET}")
        
        return True
    
    def display_analysis_results(self, user_data, weak_passwords, analysis_stats):
        """عرض نتائج التحليل"""
        self.clear_screen()
        self.print_banner()
        self.print_section("Analysis results", Colors.GREEN)
        
        # Information Summary
        print(f"\n{self.colors.CYAN}{self.colors.BOLD}[👤] Information Summary:{self.colors.RESET}")
        print(f"  {self.colors.BLUE}↳ Name: {self.colors.WHITE}{user_data['name']}{self.colors.RESET}")
        
        if user_data['birth_year']:
            age = datetime.now().year - int(user_data['birth_year'])
            print(f"  {self.colors.BLUE}↳ Approximate age: {self.colors.WHITE}{age} age{self.colors.RESET}")
        
        if user_data['hobbies']:
            print(f"  {self.colors.BLUE}↳ Hobbies: {self.colors.WHITE}{user_data['hobbies']}{self.colors.RESET}")
        
        print(f"  {self.colors.BLUE}↳ Possible weak passwords: {self.colors.WHITE}{analysis_stats['total_weak_passwords']}{self.colors.RESET}")
        
        # عرض كلمات المرور الضعيفة
        if weak_passwords:
            self.print_section("Possible weak passwords 🚨", Colors.RED)
            
            print(f"\n{self.colors.YELLOW}[i] These are passwords that can be easily guessed.:{self.colors.RESET}\n")
            
            # عرض كلمات المرور في أعمدة
            for i, password in enumerate(weak_passwords, 1):
                color = self.colors.RED if i <= 10 else self.colors.YELLOW if i <= 20 else self.colors.WHITE
                print(f"  {color}[{i:02d}] {password:<25}{self.colors.RESET}", end="")
                if i % 2 == 0:
                    print()
            
            if len(weak_passwords) % 2 != 0:
                print()
        else:
            self.print_section("Analysis results ✅", Colors.GREEN)
            print(f"\n{self.colors.GREEN}[✓] No obvious weak passwords were found!{self.colors.RESET}")
        
        # Analysis statistics
        self.print_section("Analysis statistics 📊", Colors.CYAN)
        
        print(f"\n{self.colors.BLUE}• Possible weak passwords: {self.colors.WHITE}{analysis_stats['total_weak_passwords']}{self.colors.RESET}")
        print(f"{self.colors.BLUE}• Level of risk: {self.get_risk_level(analysis_stats['total_weak_passwords'])}{self.colors.RESET}")
        print(f"{self.colors.BLUE}• Personal information used: {self.colors.WHITE}{'Yes' if analysis_stats['personal_info_used'] else 'No'}{self.colors.RESET}")
    
    def get_risk_level(self, weak_passwords_count):
        """تحديد مستوى الخطورة"""
        if weak_passwords_count == 0:
            return f"{self.colors.GREEN}Low{self.colors.RESET}"
        elif weak_passwords_count <= 10:
            return f"{self.colors.YELLOW}Medium{self.colors.RESET}"
        elif weak_passwords_count <= 20:
            return f"{self.colors.RED}High{self.colors.RESET}"
        else:
            return f"{self.colors.RED}{self.colors.BOLD}Very dangerous{self.colors.RESET}"
    
    def display_recommendations(self, weak_passwords_count):
        """عرض التوصيات الأمنية"""
        self.print_section("توصيات أمنية 💡", Colors.MAGENTA)
        
        recommendations = [
            "Avoid using personal information in passwords.",
            "Use passwords that are at least 12 characters long.",
            "Mix uppercase and lowercase letters, numbers, and symbols.",
            "Do not reuse passwords across multiple accounts.",
            "Use a reliable password manager.",
            "Enable two-factor authentication (2FA) when available."
        ]
        
        if weak_passwords_count > 10:
            recommendations.insert(0, "⚠️  Your personal information allows for the generation of many weak passwords.")
        
        print()
        for i, recommendation in enumerate(recommendations, 1):
            print(f"  {self.colors.GREEN}[{i}] {recommendation}{self.colors.RESET}")
    
    def generate_strong_password_demo(self):
        """Show an example of a strong password"""
        self.print_section("Strong password example 🔐", Colors.GREEN)
        
        strong_password = self.analyzer.generate_strong_password(16)
        strength_analysis = self.analyzer.analyze_password_strength(strong_password)
        
        print(f"\n{self.colors.CYAN}Suggested password: {self.colors.WHITE}{self.colors.BOLD}{strong_password}{self.colors.RESET}")
        print(f"{self.colors.BLUE}level of strength: {self.colors.GREEN}{strength_analysis['strength']}{self.colors.RESET}")
        print(f"{self.colors.BLUE}length: {self.colors.WHITE}{strength_analysis['length']} character{self.colors.RESET}")
        
        # Power details
        print(f"\n{self.colors.CYAN}Power details:{self.colors.RESET}")
        details = [
            ("capital letters", strength_analysis.get('has_upper', False)),
            ("small letters", strength_analysis.get('has_lower', False)),
            ("num", strength_analysis.get('has_digit', False)),
            ("Special codes", strength_analysis.get('has_special', False))
        ]
        
        for detail, exists in details:
            status = f"{self.colors.GREEN}✓{self.colors.RESET}" if exists else f"{self.colors.RED}✗{self.colors.RESET}"
            print(f"  {status} {detail}")
    
    def save_results(self, user_data, weak_passwords, filename=None):
        """save results"""
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"guesspass_results_{timestamp}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("=" * 60 + "\n")
                f.write("GuessPass - Password analysis results\n")
                f.write("Developed by: r7al38\n")
                f.write(f"Date of analysis: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 60 + "\n\n")
                
                f.write("Inputted information:\n")
                f.write(f"  Name: {user_data.get('name', 'undefined')}\n")
                f.write(f"  Date of birth: {user_data.get('birth_day', 'undefined')}/{user_data.get('birth_month', '')}/{user_data.get('birth_year', '')}\n")
                f.write(f"  Hobbies: {user_data.get('hobbies', 'undefined')}\n")
                f.write(f"  Pet name: {user_data.get('pet_name', 'undefined')}\n\n")
                
                f.write("Possible weak passwords:\n")
                for i, password in enumerate(weak_passwords, 1):
                    f.write(f"  [{i:02d}] {password}\n")
                
                f.write(f"\nTotal passwords: {len(weak_passwords)}\n")
                f.write("=" * 60 + "\n")
            
            print(f"\n{self.colors.GREEN}[✓] The results were saved in: {filename}{self.colors.RESET}")
            return True
        except Exception as e:
            print(f"{self.colors.RED}[!] Error saving results: {e}{self.colors.RESET}")
            return False
    
    def show_menu(self):
        """Show main menu"""
        self.print_section("Main menu", Colors.MAGENTA)
        
        menu_options = [
            "Start a new analysis",
            "Generate a strong password",
            "Analyzing a specific password",
            "About the tool",
            "Exit"
        ]
        
        print()
        for i, option in enumerate(menu_options, 1):
            print(f"  {self.colors.CYAN}[{i}] {option}{self.colors.RESET}")
        
        return self.get_user_input("Choose an option", input_type="number")
    
    def analyze_specific_password(self):
        """Analyzing a specific password"""
        self.print_section("Analyzing a specific password", Colors.BLUE)
        
        password = self.get_user_input("Enter the password to analyze it", required=True)
        analysis = self.analyzer.analyze_password_strength(password)
        
        print(f"\n{self.colors.CYAN}Password analysis results:{self.colors.RESET}")
        print(f"  {self.colors.BLUE}↳ The word: {self.colors.WHITE}{password}{self.colors.RESET}")
        print(f"  {self.colors.BLUE}↳ Length: {self.colors.WHITE}{analysis['length']} character{self.colors.RESET}")
        print(f"  {self.colors.BLUE}↳ level of strength: {analysis['strength']}{self.colors.RESET}")
        print(f"  {self.colors.BLUE}↳ points: {self.colors.WHITE}{analysis['score']}/4{self.colors.RESET}")
        
        if analysis['feedback']:
            print(f"\n{self.colors.YELLOW}Notte:{self.colors.RESET}")
            for feedback in analysis['feedback']:
                print(f"  • {feedback}")
    
    def about_tool(self):
        """عرض معلومات عن الأداة"""
        self.clear_screen()
        self.print_banner()
        self.print_section("About GuessPass", Colors.CYAN)
        
        about_text = f"""
{self.colors.WHITE}
GuessPass is a command-line password analyzer, developed with the goal of:

{self.colors.GREEN}🎯 Goals:{self.colors.WHITE}
• Increased security awareness regarding passwords
• Helping users understand the risks of personal information
• Providing an educational tool for cybersecurity enthusiasts

{self.colors.GREEN}🛡️  Principles of the tool:{self.colors.WHITE}
• {self.colors.GREEN}Complete privacy:{self.colors.WHITE} No data is saved
• {self.colors.GREEN}Educational:{self.colors.WHITE} For educational and awareness purposes only
• {self.colors.GREEN}Open source:{self.colors.WHITE} The source code is available to everyone.

{self.colors.GREEN}📞 For developers:{self.colors.WHITE}
• Developer: r7al38
• Language: Python 3

{self.colors.YELLOW}⚠️  warning:{self.colors.WHITE}
This tool is for educational and security awareness purposes only.

It should not be used for illegal or harmful purposes..
{self.colors.RESET}
"""
        print(about_text)
        
        input(f"\n{self.colors.CYAN}Press Enter to return to the main menu...{self.colors.RESET}")
    
    def exit_tool(self):
        """exit"""
        self.print_section("Thank you for using GuessPass", Colors.GREEN)
        print(f"\n{self.colors.CYAN}Developed by: {self.colors.MAGENTA}r7al38{self.colors.RESET}")
        print(f"{self.colors.YELLOW}Contact us to contribute or report errors{self.colors.RESET}\n")
        sys.exit(0)
    
    def main(self):
        """الدالة الرئيسية"""
        try:
            self.clear_screen()
            self.print_banner()
            
            while True:
                choice = self.show_menu()
                
                if choice == '1':
                    # بدء تحليل جديد
                    user_data = self.collect_user_data()
                    
                    if self.validate_data(user_data):
                        # تحليل البيانات
                        weak_passwords = self.analyzer.generate_weak_passwords(user_data)
                        
                        # إحصائيات التحليل
                        analysis_stats = {
                            'total_weak_passwords': len(weak_passwords),
                            'personal_info_used': any([
                                user_data['name'],
                                user_data['hobbies'],
                                user_data['pet_name'],
                                user_data['birth_year']
                            ])
                        }
                        
                        # عرض النتائج
                        self.display_analysis_results(user_data, weak_passwords, analysis_stats)
                        self.display_recommendations(len(weak_passwords))
                        
                        # عرض كلمة مرور قوية
                        self.generate_strong_password_demo()
                        
                        # حفظ النتائج
                        save_choice = self.get_user_input("Do you want to save the results to a file? (y/n)", required=False)
                        if save_choice.lower() in ['y', 'yes', 'نعم']:
                            self.save_results(user_data, weak_passwords)
                        
                        input(f"\n{self.colors.CYAN}Press Enter to continue...{self.colors.RESET}")
                
                elif choice == '2':
                    # توليد كلمة مرور قوية
                    self.clear_screen()
                    self.print_banner()
                    self.generate_strong_password_demo()
                    input(f"\n{self.colors.CYAN}Press Enter to continue...{self.colors.RESET}")
                
                elif choice == '3':
                    # تحليل كلمة مرور محددة
                    self.clear_screen()
                    self.print_banner()
                    self.analyze_specific_password()
                    input(f"\n{self.colors.CYAN}Press Enter to continue...{self.colors.RESET}")
                
                elif choice == '4':
                    # حول الأداة
                    self.about_tool()
                
                elif choice == '5':
                    # الخروج
                    self.exit_tool()
                
                else:
                    print(f"{self.colors.RED}[!] Incorrect choice{self.colors.RESET}")
                    time.sleep(1)
                
                self.clear_screen()
                self.print_banner()
        
        except KeyboardInterrupt:
            self.exit_tool()
        except Exception as e:
            print(f"{self.colors.RED}[!] Unexpected error: {e}{self.colors.RESET}")
            self.exit_tool()

if __name__ == "__main__":
    try:
        tool = GuessPass()
        tool.main()
    except KeyboardInterrupt:
        print(f"\n{Colors.RED}[!] The tool has been disabled.{Colors.RESET}")
        sys.exit(0)
