export default function HighlightImage({src}, {x}, {y}, {alt}){
    return (
    <>
        <img src={src} alt={alt}>
            <div className="rectangle" />
        </img>
    </> 
    )
}