import React, { Component } from 'react';
import PropTypes from 'prop-types';

import Table from 'react-bootstrap/Table'

class HighScoreTable extends Component {
	render() {
		return (
			<Table striped hover bordered>
				<thead>
					<tr>
						<th>Rank</th>
						<th>Name</th>
						<th>Score</th>
					</tr>
				</thead>
				<tbody>
					{
						this.props.data.map((item, i) => {
							return(
									<tr>
										<td>{i + 1}</td>
										<td>{item.name}</td>
										<td>{item.score}</td>
									</tr>
								)
						})
					}
				</tbody>
			</Table>
		);
	}
}

HighScoreTable.propTypes = {
	data: PropTypes.object.isRequired
}

export default HighScoreTable;
