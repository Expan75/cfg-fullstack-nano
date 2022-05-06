export const PokemonListItem = (props) => {
    console.log('PokemonListItemProps: ', props)
    return (
        <>
            <p>{props.name}, {props.url}</p>
        </>
    )
};