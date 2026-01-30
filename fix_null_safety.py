#!/usr/bin/env python3
"""
Travel Verse - Automated Null Safety Migration Script
This script fixes common null safety issues in Flutter/Dart projects
"""

import os
import re
from pathlib import Path

def fix_dart_file(filepath):
    """Fix null safety issues in a single Dart file"""
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix 1: Replace @required with required
    content = re.sub(r'@required\s+this\.', 'required this.', content)
    
    # Fix 2: Replace Key key with Key? key in constructors
    content = re.sub(r'(\{\s*)Key key,', r'\1Key? key,', content)
    
    # Fix 3: Replace FlatButton with TextButton
    content = content.replace('FlatButton(', 'TextButton(')
    
    # Fix 4: Replace RaisedButton with ElevatedButton
    content = content.replace('RaisedButton(', 'ElevatedButton(')
    
    # Fix 5: Replace OutlineButton with OutlinedButton
    content = content.replace('OutlineButton(', 'OutlinedButton(')
    
    # Fix 6: Replace overflow: Overflow.visible with clipBehavior: Clip.none
    content = re.sub(r'overflow:\s*Overflow\.visible', 'clipBehavior: Clip.none', content)
    
    # Fix 7: Replace old TextTheme styles with new ones
    theme_replacements = {
        '.headline1': '.displayLarge',
        '.headline2': '.displayMedium',
        '.headline3': '.displaySmall',
        '.headline4': '.headlineMedium',
        '.headline5': '.headlineSmall',
        '.headline6': '.titleLarge',
        '.subtitle1': '.titleMedium',
        '.subtitle2': '.titleSmall',
        '.bodyText1': '.bodyLarge',
        '.bodyText2': '.bodyMedium',
        '.caption': '.bodySmall',
    }
    
    for old, new in theme_replacements.items():
        content = content.replace(old, new)
    
    # Only write if content changed
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_size_config(filepath):
    """Special handling for size_config.dart"""
    
    if not os.path.exists(filepath):
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Add 'late' keyword to static fields that aren't initialized
    replacements = [
        ('static MediaQueryData _mediaQueryData;', 'static late MediaQueryData _mediaQueryData;'),
        ('static double screenWidth;', 'static late double screenWidth;'),
        ('static double screenHeight;', 'static late double screenHeight;'),
        ('static double defaultSize;', 'static late double defaultSize;'),
        ('static Orientation orientation;', 'static late Orientation orientation;'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
    
    # Fix Key parameter
    content = re.sub(r'(\{\s*)Key key,', r'\1Key? key,', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def fix_app_bar(filepath):
    """Special handling for app_bar.dart"""
    
    if not os.path.exists(filepath):
        return False
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    
    # Fix the title parameter to be required
    content = re.sub(
        r'\{bool isTransparent = false,\s*String title\}',
        '{bool isTransparent = false, required String title}',
        content
    )
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

def main():
    """Main function to process all Dart files"""
    
    print("🚀 Travel Verse - Null Safety Migration Script")
    print("=" * 50)
    
    # Get the project root (assuming script is run from project directory)
    project_root = Path.cwd()
    lib_dir = project_root / 'lib'
    
    if not lib_dir.exists():
        print("❌ Error: 'lib' directory not found!")
        print("Please run this script from your Flutter project root directory.")
        return
    
    print(f"📁 Project root: {project_root}")
    print(f"📂 Processing files in: {lib_dir}")
    print()
    
    # Special files with custom fixes
    size_config_path = lib_dir / 'size_config.dart'
    app_bar_path = lib_dir / 'components' / 'app_bar.dart'
    
    files_fixed = 0
    
    # Fix size_config.dart
    if fix_size_config(size_config_path):
        print(f"✅ Fixed: {size_config_path}")
        files_fixed += 1
    
    # Fix app_bar.dart
    if fix_app_bar(app_bar_path):
        print(f"✅ Fixed: {app_bar_path}")
        files_fixed += 1
    
    # Process all other Dart files
    for dart_file in lib_dir.rglob('*.dart'):
        # Skip files we already handled
        if dart_file in [size_config_path, app_bar_path]:
            continue
            
        if fix_dart_file(dart_file):
            print(f"✅ Fixed: {dart_file.relative_to(project_root)}")
            files_fixed += 1
    
    print()
    print("=" * 50)
    print(f"✨ Migration complete! Fixed {files_fixed} files.")
    print()
    print("Next steps:")
    print("1. Run: flutter clean")
    print("2. Run: flutter pub get")
    print("3. Run: flutter run")
    print()
    print("If you still have errors, check the travel_verse_fixes.md file")
    print("for manual fixes that may be needed.")

if __name__ == '__main__':
    main()
