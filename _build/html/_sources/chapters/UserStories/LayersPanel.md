# Layers Panel User Story

## Overview
As a designer creating App Store promotional screenshots, I want a layers panel to manage all elements on my canvas so that I can easily control visibility, organize my design, and quickly select elements without hunting through the canvas.

## User Personas
- **Sarah**: A mobile app designer creating promotional screenshots for multiple device sizes
- **Marcus**: A marketing designer who needs to create localized screenshots in different languages
- **Emma**: A freelance designer working on multiple client projects with complex layouts

## Key Features

### 1. Viewing All Layers
**Given** I have multiple elements on my canvas (devices, text, images)  
**When** I look at the left sidebar  
**Then** I see a hierarchical list of all elements in their render order (devices at bottom, text at top)

### 2. Toggling Visibility
**Given** I have a layer visible on the canvas  
**When** I click the checkbox next to the layer name  
**Then** the element disappears from the canvas but remains in the layers list  
**And** the checkbox shows an empty square  
**And** I cannot select the hidden element by clicking on the canvas

### 3. Selecting Elements
**Given** I have multiple elements on my canvas  
**When** I click on a layer in the panel  
**Then** the element is selected on the canvas with a highlight border  
**And** the properties panel shows the element's settings  
**And** the layer row shows a selection highlight

### 4. Renaming Layers
**Given** I want to organize my layers with meaningful names  
**When** I double-click on a layer name  
**Then** the name becomes editable  
**And** I can type a new name  
**And** pressing Enter or clicking away saves the change

### 5. Deleting Layers
**Given** I have selected a layer  
**When** I click the trash icon that appears on selection  
**Then** the element is removed from both the canvas and layers panel  
**And** the selection is cleared

### 6. Visual Feedback
- **Layer Types**: Each layer shows an icon indicating its type:
  - 📱 `rectangle.on.rectangle` for device frames
  - 🔤 `textformat` for text elements
  - 🖼️ `photo` for images
- **Alternating Rows**: Even rows have a subtle background for better readability
- **Selection State**: Selected layers have a blue tinted background
- **Empty State**: When no layers exist, helpful text guides users to add elements

## Interaction Scenarios

### Scenario 1: Creating a Multi-Device Screenshot
Sarah is creating promotional screenshots showing her app on multiple devices:

1. She adds an iPhone 16 Plus to the canvas
2. The layers panel shows "iPhone 16 Plus" with a device icon
3. She adds a screenshot to the device
4. She duplicates the setup and changes to iPad
5. She renames the layers to "iPhone - Home Screen" and "iPad - Home Screen"
6. She temporarily hides the iPad while working on iPhone positioning

### Scenario 2: Managing Text Overlays
Marcus needs to add promotional text in multiple languages:

1. He adds text saying "Revolutionary New Features"
2. The layer appears as "Text Layer 1"
3. He renames it to "English - Hero Text"
4. He duplicates it and changes the text to Spanish
5. He uses visibility toggles to switch between languages
6. He can quickly select text elements from the panel without clicking small text on canvas

### Scenario 3: Complex Layout Organization
Emma is working on a screenshot with many elements:

1. She has 3 devices, 5 text elements, and 2 decorative images
2. She uses descriptive names: "iPhone - Onboarding", "CTA Button Text", "Background Pattern"
3. She hides background elements while positioning foreground text
4. She quickly finds and deletes outdated elements using the layers panel
5. She double-checks all elements are visible before exporting

## Technical Behavior

### Selection Synchronization
- Clicking a layer selects the corresponding canvas element
- Selecting an element on canvas highlights its layer
- Only one element can be selected at a time across all types

### Visibility Rules
- Hidden elements cannot be selected on canvas
- Hidden elements don't respond to clicks or drags
- Visibility state persists when saving/loading documents

### Naming Conventions
- Device frames default to their device type name
- Text layers are numbered: "Text Layer 1", "Text Layer 2"
- Images use their filename or "Image 1", "Image 2" if unnamed

### Render Order
Layers are displayed and rendered in this order (bottom to top):
1. Device frames (bottom layer)
2. Image elements (middle layer)
3. Text elements (top layer)

## Accessibility Considerations
- All interactive elements have descriptive help tags
- Keyboard navigation through layers list
- Visual feedback for all interactions
- Clear icons that work in both light and dark themes

## Future Enhancements
- Drag and drop reordering within element types
- Layer grouping/folders for complex projects
- Lock layers to prevent accidental changes
- Duplicate layer functionality
- Multi-select for bulk operations

## Success Metrics
- Users can find and select elements 3x faster than clicking on canvas
- 90% of users successfully use visibility toggles in their first session
- Reduced accidental element deletion by 50% due to explicit delete action
- Increased project organization with 80% of users renaming at least one layer

## Testing Considerations

### Unit Tests (@Test)
```swift
@Test("Layer visibility toggle updates element state")
func testVisibilityToggle() async {
    let appState = AppState()
    let device = DeviceFrame()
    appState.devices.append(device)
    
    #expect(device.isVisible == true)
    appState.toggleVisibility(for: device.id)
    #expect(appState.devices.first?.isVisible == false)
}

@Test("Layer deletion removes element and clears selection")
func testLayerDeletion() async {
    let appState = AppState()
    appState.addTextElement()
    let textId = appState.textElements.first?.id
    
    #expect(appState.selectedTextId == textId)
    appState.deleteElement(id: textId!)
    
    #expect(appState.textElements.isEmpty)
    #expect(appState.selectedTextId == nil)
}

@Test("Auto-naming generates sequential numbers", 
      arguments: [1, 2, 3, 5, 10])
func testLayerAutoNaming(count: Int) async {
    let appState = AppState()
    
    for i in 1...count {
        appState.addTextElement()
        #expect(appState.textElements.last?.name == "Text Layer \(i)")
    }
}
```

### UI Tests
- Verify double-click enables name editing
- Confirm selection synchronization between panel and canvas
- Test visibility toggle affects canvas rendering
- Validate keyboard navigation through layers

## Implementation Notes
The layers panel leverages SwiftUI's declarative nature and the Observation framework for automatic UI updates. The implementation maintains clean separation between UI (LayersPanel, LayerRow) and business logic (AppState layer management methods), making it highly testable and maintainable.