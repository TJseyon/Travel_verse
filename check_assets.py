#!/usr/bin/env python3
"""
Travel Verse - Asset Diagnostic Tool
Checks if assets are properly configured
"""

import os
from pathlib import Path

def check_assets():
    print("🔍 Travel Verse - Asset Diagnostic Tool")
    print("=" * 60)
    
    project_root = Path.cwd()
    print(f"\n📁 Current directory: {project_root}")
    
    # Check if we're in the right directory
    if not (project_root / 'pubspec.yaml').exists():
        print("\n❌ ERROR: pubspec.yaml not found!")
        print("   Please run this script from your project root directory:")
        print("   C:\\Users\\seyon\\AndroidStudioProjects\\travel_verse\\")
        return
    
    print("✅ Found pubspec.yaml")
    
    # Check assets folder
    assets_dir = project_root / 'assets'
    images_dir = assets_dir / 'images'
    icons_dir = assets_dir / 'icons'
    
    print(f"\n📂 Checking folder structure...")
    
    if not assets_dir.exists():
        print("❌ assets/ folder NOT FOUND")
        print("   Creating it now...")
        assets_dir.mkdir(exist_ok=True)
    else:
        print("✅ assets/ folder exists")
    
    if not images_dir.exists():
        print("❌ assets/images/ folder NOT FOUND")
        print("   Creating it now...")
        images_dir.mkdir(exist_ok=True)
    else:
        print("✅ assets/images/ folder exists")
    
    if not icons_dir.exists():
        print("❌ assets/icons/ folder NOT FOUND")
        print("   Creating it now...")
        icons_dir.mkdir(exist_ok=True)
    else:
        print("✅ assets/icons/ folder exists")
    
    # Check for required image files
    print(f"\n🖼️  Checking image files in: {images_dir}")
    
    required_images = [
        'profile.jpg',
        'home_bg.jpg',
        'james.jpg',
        'marry.jpg',
        'John.jpg',
        'rosy.jpg',
        'Red_Mountains.jpg',
        'Magical_World.jpg'
    ]
    
    missing_images = []
    for img in required_images:
        img_path = images_dir / img
        if img_path.exists():
            size = img_path.stat().st_size
            print(f"  ✅ {img} ({size} bytes)")
        else:
            print(f"  ❌ {img} - NOT FOUND")
            missing_images.append(img)
    
    # Check for SVG icons
    print(f"\n🎨 Checking SVG icons in: {icons_dir}")
    
    required_icons = ['calendar.svg', 'chat.svg', 'friendship.svg']
    missing_icons = []
    
    for icon in required_icons:
        icon_path = icons_dir / icon
        if icon_path.exists():
            print(f"  ✅ {icon}")
        else:
            print(f"  ❌ {icon} - NOT FOUND")
            missing_icons.append(icon)
    
    # Check pubspec.yaml
    print(f"\n📄 Checking pubspec.yaml...")
    
    pubspec_path = project_root / 'pubspec.yaml'
    with open(pubspec_path, 'r', encoding='utf-8') as f:
        pubspec_content = f.read()
    
    if 'assets/images/' in pubspec_content:
        print("  ✅ assets/images/ is declared in pubspec.yaml")
    else:
        print("  ❌ assets/images/ NOT declared in pubspec.yaml")
    
    if 'assets/icons/' in pubspec_content:
        print("  ✅ assets/icons/ is declared in pubspec.yaml")
    else:
        print("  ❌ assets/icons/ NOT declared in pubspec.yaml")
    
    # Check indentation
    print(f"\n🔍 Checking pubspec.yaml indentation...")
    lines = pubspec_content.split('\n')
    
    flutter_found = False
    assets_found = False
    correct_indentation = True
    
    for i, line in enumerate(lines, 1):
        if line.strip().startswith('flutter:'):
            flutter_found = True
            print(f"  Line {i}: flutter: ✅")
        
        if 'assets:' in line and flutter_found:
            assets_found = True
            spaces_before_assets = len(line) - len(line.lstrip())
            if spaces_before_assets == 2:
                print(f"  Line {i}: assets: ✅ (2 spaces)")
            else:
                print(f"  Line {i}: assets: ❌ ({spaces_before_assets} spaces, should be 2)")
                correct_indentation = False
        
        if '- assets/images/' in line:
            spaces = len(line) - len(line.lstrip())
            if spaces == 4:
                print(f"  Line {i}: - assets/images/ ✅ (4 spaces)")
            else:
                print(f"  Line {i}: - assets/images/ ❌ ({spaces} spaces, should be 4)")
                correct_indentation = False
    
    # Summary
    print("\n" + "=" * 60)
    print("📊 SUMMARY:")
    print("=" * 60)
    
    if missing_images:
        print(f"\n❌ Missing {len(missing_images)} image(s):")
        for img in missing_images:
            print(f"   - {img}")
    else:
        print("\n✅ All required images are present!")
    
    if missing_icons:
        print(f"\n❌ Missing {len(missing_icons)} icon(s):")
        for icon in missing_icons:
            print(f"   - {icon}")
    else:
        print("\n✅ All required icons are present!")
    
    if not correct_indentation:
        print("\n❌ pubspec.yaml has indentation issues!")
        print("\n📝 Your pubspec.yaml should look like this:")
        print("""
flutter:
  uses-material-design: true

  assets:
    - assets/images/
    - assets/icons/
""")
    
    print("\n💡 Next steps:")
    if missing_images or missing_icons:
        print("1. Add the missing files to the correct folders")
    if not correct_indentation:
        print("2. Fix the indentation in pubspec.yaml")
    print("3. Run: flutter clean")
    print("4. Run: flutter pub get")
    print("5. Run: flutter run")

if __name__ == '__main__':
    check_assets()
