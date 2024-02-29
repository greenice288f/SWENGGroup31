import styled from "styled-components";

const theme = {
    blue: {
        default: "#3f51b5",
        hover: "#283593",
    },
    red: {
        default: "#D52941",
        hover: "#B51E32",
    },
};

const Button = styled.button`
    background-color: ${(props) => theme[props.theme].default};
    color: white;
    padding: 15px 35px;
    border-radius: 10px;
    outline: 0;
    border: 0;
    margin: 10px 5px;
    cursor: pointer;
    box-shadow: 0px 2px 2px lightgray;
    transition: ease background-color 250ms;
    &:hover {
        background-color: ${(props) => theme[props.theme].hover};
    }
    &:disabled {
        cursor: default;
        opacity: 0.7;
    }
`;

Button.defaultProps = {
    theme: 'blue'
};

export default Button;