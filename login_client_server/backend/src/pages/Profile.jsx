import { ProfileContext } from '../context/ProfileContext.jsx';
import { useContext } from 'react';
import { useNavigate } from 'react-router';

export default function Profile() {
    //Extract user info and logout function from context
    const { user, logout } = useContext(ProfileContext);
    const navigate = useNavigate();


    //Handler for logout button
    const handleLogout = () => {
        const confirmation = confirm('Are you sure you want to logout?');
        if(confirmation) {
            logout(); //remove token from localStorage
            navigate('/'); // redirect to home page (login screen)
        }
    };

    return (
        <>
            {/* Display a greeting using the user's name */}
            <h1 className='greeting'>
                Hello, {user.user || 'Guest'}!
            </h1>

            {/* Logout button*/}
            <button onClick={handleLogout} className="login-btn logout-btn">
                Logout
            </button>
        </>
    );
}