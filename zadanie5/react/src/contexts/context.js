import React, { useState } from "react";

export const ShopContext = React.createContext([]);

export const ShopContextProvider= ({children}) => {
    const [cart, setCart] = useState([]);

    const addCart = (product) => setCart([...cart, product]);

    return (
        <ShopContext.Provider value={{cart, addCart}}>
            {children}
        </ShopContext.Provider>
    );
}








