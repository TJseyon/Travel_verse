#!/usr/bin/env python3
"""
Travel Verse - Asset Placeholder Generator
Creates placeholder images for missing assets
"""

import os
from pathlib import Path

def create_placeholder_image(filepath, width=400, height=300, color="#CCCCCC", text=""):
    """Create a simple SVG placeholder image"""
    
    svg_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    <rect width="100%" height="100%" fill="{color}"/>
    <text x="50%" y="50%" font-family="Arial" font-size="20" fill="#666666" text-anchor="middle" dominant-baseline="middle">
        {text}
    </text>
</svg>'''
    
    # Save as jpg would require PIL/Pillow library
    # For now, we'll create a simple text file that tells user what to do
    return svg_content

def create_placeholder_svg_icon(filepath, icon_type):
    """Create a simple SVG icon"""
    
    icons = {
        'calendar': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <rect x="3" y="4" width="18" height="18" rx="2" ry="2"></rect>
    <line x1="16" y1="2" x2="16" y2="6"></line>
    <line x1="8" y1="2" x2="8" y2="6"></line>
    <line x1="3" y1="10" x2="21" y2="10"></line>
</svg>''',
        'chat': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path>
</svg>''',
        'friendship': '''<svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
    <path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"></path>
    <circle cx="9" cy="7" r="4"></circle>
    <path d="M23 21v-2a4 4 0 0 0-3-3.87"></path>
    <path d="M16 3.13a4 4 0 0 1 0 7.75"></path>
</svg>'''
    }
    
    return icons.get(icon_type, icons['calendar'])

def main():
    print("🎨 Travel Verse - Asset Placeholder Generator")
    print("=" * 60)
    
    project_root = Path.cwd()
    
    # Create directories
    images_dir = project_root / 'assets' / 'images'
    icons_dir = project_root / 'assets' / 'icons'
    
    images_dir.mkdir(parents=True, exist_ok=True)
    icons_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"\n✅ Created directory: {images_dir}")
    print(f"✅ Created directory: {icons_dir}")
    
    # Create SVG icons
    icons_to_create = {
        'calendar.svg': 'calendar',
        'chat.svg': 'chat',
        'friendship.svg': 'friendship'
    }
    
    print("\n📦 Creating SVG icons...")
    for filename, icon_type in icons_to_create.items():
        filepath = icons_dir / filename
        svg_content = create_placeholder_svg_icon(filepath, icon_type)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        
        print(f"  ✅ Created: {filename}")
    
    # Create instructions for images
    print("\n📝 Image placeholders needed:")
    print("\nYou need to manually add these jpg images to assets/images/:")
    
    images_needed = [
        'profile.jpg',
        'home_bg.jpg',
        'james.jpg',
        'marry.jpg',
        'John.jpg',
        'rosy.jpg',
        'Red_Mountains.jpg',
        'Magical_World.jpg'
    ]
    
    for img in images_needed:
        print(f"  📸 {img}")
    
    # Create a README in images folder
    readme_content = """# Travel Verse Images

Please add the following images to this folder:

## Profile Images (People)
- profile.jpg (400x400 px recommended)
- james.jpg (400x400 px recommended)
- marry.jpg (400x400 px recommended)
- John.jpg (400x400 px recommended)
- rosy.jpg (400x400 px recommended)

## Travel Destination Images
- Red_Mountains.jpg (800x600 px recommended)
- Magical_World.jpg (800x600 px recommended)

## Background
- home_bg.jpg (1200x800 px recommended)

## Where to get free images:

1. **Unsplash.com** - High quality free photos
   - Search: "mountain", "fantasy landscape", "portrait"

2. **Pexels.com** - Free stock photos
   - Search: "travel destination", "landscape"

3. **Placeholder Images (Quick Fix)**
   - Visit: https://via.placeholder.com/400x300.jpg
   - Download and rename for each image

## Quick Download Commands:

You can use these PowerShell commands to download placeholder images:

```powershell
Invoke-WebRequest -Uri "https://via.placeholder.com/400x400/4A90E2/FFFFFF?text=Profile" -OutFile "profile.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/400x400/E94B3C/FFFFFF?text=James" -OutFile "james.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/400x400/6AB187/FFFFFF?text=Marry" -OutFile "marry.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/400x400/F39C12/FFFFFF?text=John" -OutFile "John.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/400x400/E84393/FFFFFF?text=Rosy" -OutFile "rosy.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/800x600/8E44AD/FFFFFF?text=Red+Mountains" -OutFile "Red_Mountains.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/800x600/3498DB/FFFFFF?text=Magical+World" -OutFile "Magical_World.jpg"
Invoke-WebRequest -Uri "https://via.placeholder.com/1200x800/2C3E50/FFFFFF?text=Home+Background" -OutFile "home_bg.jpg"
```

Run these commands from this directory in PowerShell!
"""
    
    readme_path = images_dir / 'README.md'
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(readme_content)
    
    print(f"\n✅ Created guide: {readme_path}")
    
    print("\n" + "=" * 60)
    print("✨ Setup complete!")
    print("\nNext steps:")
    print("1. Navigate to: assets/images/")
    print("2. Read the README.md file")
    print("3. Add the required jpg images")
    print("4. Run: flutter clean && flutter pub get && flutter run")
    print("\nQuick fix: Run the PowerShell commands in the README to download placeholders!")

if __name__ == '__main__':
    main()
