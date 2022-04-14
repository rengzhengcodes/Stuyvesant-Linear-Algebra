import lin_reg

def collapse_3D_2D_manual(m3D:np.ndarray) -> np.ndarray:
	if m3D.ndim == 3:
		arr = list()
		m3D = m3D.tolist()

		for row in n3D:
			row = list()
			for column in row:
				for height in column:
					row.append(height)
			arr.append(list)

		return np.asarray(arr)
	else:
		raise ValueError("Expected 3D array, got " + m3D.dim)
