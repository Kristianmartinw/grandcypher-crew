import React, { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux'
import { Redirect } from 'react-router-dom';
import { signUp } from '../../store/session';

const SignUpForm = ({ setShowModal }) => {
  const [errors, setErrors] = useState([]);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [repeatPassword, setRepeatPassword] = useState('');
  const user = useSelector(state => state.session.user);
  const dispatch = useDispatch();

  const onSignUp = async (e) => {
    e.preventDefault();
    if (password === repeatPassword) {
      const data = await dispatch(signUp(username, email, password));
      if (data) {
        setErrors(data)
      } else {
        setShowModal(false)
      }
    } else {
      setErrors(['Passwords do not match'])
    }
  };

  const updateUsername = (e) => {
    setUsername(e.target.value);
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  const updateRepeatPassword = (e) => {
    setRepeatPassword(e.target.value);
  };

  if (user) {
    return <Redirect to='/' />;
  }

  return (
    <form onSubmit={onSignUp}>
      <div className='sign-up-form'>
        <div className='errors'>
          {errors.map((error, ind) => (
            <div key={ind}>{error}</div>
          ))}
        </div>
        {errors.length > 0 &&
          <img className='error-papyrus' alt=''
            src={'https://grandhcypher-crew.s3.us-west-1.amazonaws.com/images/error-papyrus.png'}></img>
        }
        <div>
          <label>Username: </label>
          <input
            type='text'
            name='username'
            onChange={updateUsername}
            value={username}
            maxLength={20}
          ></input>
        </div>
        <div>
          <label>Email: </label>
          <input
            type='text'
            name='email'
            onChange={updateEmail}
            value={email}
            maxLength={50}
          ></input>
        </div>
        <div>
          <label>Password: </label>
          <input
            type='password'
            name='password'
            onChange={updatePassword}
            value={password}
            required={true}
            maxLength={20}
          ></input>
        </div>
        <div>
          <label>Repeat Password: </label>
          <input
            type='password'
            name='repeat_password'
            onChange={updateRepeatPassword}
            value={repeatPassword}
            required={true}
            maxLength={20}
          ></input>
        </div>
        <button type='submit'>Sign Up</button>
      </div>
    </form>
  );
};

export default SignUpForm;
