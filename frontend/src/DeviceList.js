import React, { useState, useEffect } from 'react'; // Import React core functionalities
import { // Import Material-UI components for table display
    Table,
    TableBody,
    TableCell,
    TableContainer,
    TableHead,
    TableRow,
    Paper,
    Typography,
} from '@mui/material';

function DeviceList() {
    // State for Storing Device Data
    // -------------------------------
    const [devices, setDevices] = useState([]); // Initialize empty array to hold device data

    // Fetching and Updating Device Data (useEffect Hook)
    // -----------------------------------------------------
    useEffect(() => {
        // Function to Fetch Data from API
        // ---------------------------------
        const fetchData = async () => {
            try {
                const response = await fetch('http://localhost:8000/api/devices/'); // Make API request to fetch device data
                const data = await response.json(); // Parse the response as JSON
                setDevices(data); // Update the 'devices' state with the fetched data
            } catch (error) {
                console.error('Error fetching data:', error); // Log errors to console
            }
        };

        // Initial Data Fetch
        // --------------------
        fetchData(); // Call the function to fetch data initially

        // Continuous Data Updates (Polling)
        // ----------------------------------
        const interval = setInterval(fetchData, 5000); // Fetch data every 5 seconds
        return () => clearInterval(interval); // Clean up interval when the component unmounts
    }, []); // Empty dependency array ensures useEffect runs only once after initial render


    // Rendering the Device Table
    // ----------------------------
    return (
        <TableContainer component={Paper} style={{ margin: '20px', padding: '10px' }}> 
            {/* Container for the table with styling */}
            <Typography variant="h5" align="center" gutterBottom> 
                {/* Title of the table */}
                IoT Device List
            </Typography>
            <Table>
                <TableHead>
                    <TableRow>
                        {/* Table Headers */}
                        <TableCell>Device ID</TableCell>
                        <TableCell>Status</TableCell>
                        <TableCell>Temperature (°C)</TableCell>
                        <TableCell>Humidity (%)</TableCell>
                    </TableRow>
                </TableHead>
                <TableBody>
                    {devices.map(device => (
                        // Map device data to table rows
                        <TableRow key={device.device_id}>
                            <TableCell>{device.device_id}</TableCell>
                            <TableCell>Online</TableCell> {/* Assuming all devices are online (replace with actual status if available) */}
                            <TableCell>{device.temperature}</TableCell>
                            <TableCell>{device.humidity}</TableCell>
                        </TableRow>
                    ))}
                </TableBody>
            </Table>
        </TableContainer>
    );
}

export default DeviceList; 