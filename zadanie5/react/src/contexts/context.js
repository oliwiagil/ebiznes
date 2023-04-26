import React, { useState } from "react";

export const ShopContext = React.createContext([]);

export const ShopContextProvider= ({children}) => {
    const [cart, setCart] = useState([]);

    const addCart = (product) => setCart([...cart, product]);
    const clearCart = () => setCart([]);

    return (
        <ShopContext.Provider value={{cart, addCart, clearCart}}>
            {children}
        </ShopContext.Provider>
    );
}








