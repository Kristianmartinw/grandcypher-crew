import { useDispatch, useSelector } from 'react-redux';
import { useHistory } from 'react-router-dom';
import * as sessionActions from '../../store/session';

const DemoButton = ({ sessionUser }) => {
    const dispatch = useDispatch();
    const history = useHistory()
    useSelector(state => state.session?.user)

    let credential = 'gran@blue.io'
    let password = 'password'
    let demoLogin = () => {
        dispatch(sessionActions.login(credential, password))
        history.push('/parties')
    }

    return (
        <button onClick={demoLogin}>Demo</button >
    )
}

export default DemoButton;
