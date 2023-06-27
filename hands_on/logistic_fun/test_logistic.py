from logistic import iterate_f
import pytest
from numpy.testing import assert_allclose
import numpy as np

SEED    = np.random.randint(0,2**31)

@pytest.fixture
def random_state():
    print(f'Using seed {SEED}')
    cosa    = np.random.RandomState(SEED)
    print(cosa)
    return cosa

def test_attractor_converges(random_state):
    """Checks if converges to 1/3"""
    #xi = random_state.rand()
    #xi  = cosa
    it  = 1000
    r   = 1.5
    for _ in range(1000):
        xi = random_state.rand()
        #xi  = cosa
        result = iterate_f(it, xi, r)
        assert np.isclose(result[-1], 1/3)
