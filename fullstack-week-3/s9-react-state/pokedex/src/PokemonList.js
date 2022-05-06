import { useState, useEffect } from 'react';
import { PokemonListItem } from './PokemonListItem';

export const PokemonList = () => {

    const [offset, setOffset] = useState(0);
    const [pokemons, setPokemons] = useState([])
    const [isLoading, setIsLoading] = useState(true);

    const loadPokemon = () => {
        setOffset(offset + 20)
    };

    useEffect(() => {
        fetch(`https://pokeapi.co/api/v2/pokemon?offset=${offset}`, {
            method: 'GET', 
            headers: { 
                'Content-Type': 'application/json', 
                'Accept': 'application/json'
            }
        })
        .then(response => response.json())
        .then(data => {
            setPokemons(data.results);
            setIsLoading(false);
        })
    }, [offset]);
    
    return (
        <div>
            <h1>Pokemon</h1>
            { isLoading 
            ? <p>Loading...</p>
            : <button onClick={loadPokemon}>Load more pokemon...</button>}
            {pokemons.map((pokemon, index) => {
                return <PokemonListItem name={pokemon.name} url={pokemon.url} key={index}></PokemonListItem>
            })}
        </div>
    )
}