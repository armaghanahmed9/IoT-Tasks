// Importing Necessary Modules and Components
// --------------------------------------------
import React from 'react';               // Import the React library for building components
import DeviceList from './DeviceList';    // Import the custom DeviceList component (assuming it's in the same directory)
import { Container } from '@mui/material'; // Import Container for creating a centered layout

// Main Application Component
// ---------------------------
function App() {
    // Main application component.
    // Renders a container for the DeviceList component.
  return (
    // Container for Centering Content
    // --------------------------------
    <Container maxWidth="md">  
        {/* 
            Material UI container for layout. 
            maxWidth="md" limits the width for better readability on larger screens.
        */}
        <DeviceList />             
        {/* Render the DeviceList component */}
    </Container>
  );
}

// Exporting the App Component
// ---------------------------
export default App;                 // Export the main App component to be used by your React application