// Import hooks and dependencies
import { useState, useContext } from 'react';
import { useNavigate } from 'reat-router';
import { ProfileContext } from '../context/profileContext.jsx';
import Form from './Form.jsx';
import { registerUser, loginUser } from '../services/authServices.js';

import { StrictMode } from 'react';
import { createRoot } from 'react-dom/client';
import App from './App.jsx';
import './styles.css';

createRoot(document.getElementById('root')).render(
    <StrictMode>
        <App />
    </StrictMode>,
)


export default function Main() {
    // access login function from context
    const { login } = useContext(ProfileContext);

    //Hook from React Router to navigate pages
    const navigate = useNavigate();

    // State for form inpput
    const [ username, setUsername ] = useState('');
    const [ password, setPassword ] = useState('');

    //state to store server response or error
    const [ data, setData ] = useState('');
    const [err, setErr ] = useState(null);

    //State to toggle between login and signup/register mode
    comst [ isLoginMode, setLoginMode ] = useState(true);

    //Texts that change depending on login/signup mode
    const submitBtnText = isLoginMode ? 'Login' : 'Sign up';
    const toggleBtnText = isLoginMode ? 'sign up' : 'Login';
    const modeText = isLoginMode ? 'No account yet?' : 'Already have an account?';


    // Form submit handler
    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            // Decide which function to call based on mode
            const calledFunction = isLoginMode ? loginUser : registerUser;
            const result = await calledFunction(username, password);

            // store server response
            setData(result);


            //if login/signup was a success
            if  (result.token){
                login(result.token);  //save token in context + localStorage
                navigate('/profile'); //redirect to profile page

            }
        } catch (err) {
            console.log(err);
            setErr(err);
        }
    };

    // Toggle between login and signu modes
    const handleSignupText = () => {
        setLoginMode(prev => !prev);
    };

    //Handle input udates
    const handleUsernameInput = (e) => {
        setUsername(e.target.value);
    };

    const handlePasswordInut = (e) => {
        setPassword(e.target.value);
    };

    return (
        <>
            {/* Display server messages */}
            <div className={data.success ? 'status ok-status' : 'status error-status'}>
                {data.message}
            </div>

            {/* Our reusable form component*/}

            <Form 
                handleSubmit={handleSubmit}
                handleUsernameInput={handleUsernameInput}
                handlePasswordInput={handlePasswordInput}
                username={username}
                password={password}
                isLoginMode={isLoginMode}
                submitBtnText={submitBtnText}
            />

            {/* Toggle login/signup button*/}

            <div className='signup-wrapper'>
                <p>{modeText}</p>
                <button onClick={handleSignupText} className='login-btn signup-btn'>
                    {toggleBtnText}
                </button>
            </div>
        </>
    );
}