// INSERT THE IMPORT
import logo from '../images/logo.png';

export default function Header(){
    return (
        <header>
            // insert image tag here
            <img src={logo} alt="Logo" className="logo" />
            <h1>Login App</h1>
        </header>
    );
}