import { useSelector, useDispatch } from 'react-redux';
import { useEffect } from 'react';

const IncrementButton = () => {
    const dispatch = useDispatch()
    const currentCount = useSelector((state) => state.counterValue)

    return (
        <>
          <button
            className="incrementButton"
            onClick ={() => dispatch({ type: 'increment'})}
          >
            {currentCount ? currentCount : 0}
          </button>
        </>
    );
}

export default IncrementButton;